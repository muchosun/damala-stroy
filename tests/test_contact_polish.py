import json
import re
import unittest
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / 'index.html'


class ContactPolishTests(unittest.TestCase):
    def page(self) -> str:
        return HTML.read_text()

    def test_desktop_header_has_messenger_actions(self):
        html = self.page()
        self.assertIn('class="header-actions"', html)
        self.assertIn('aria-label="Telegram"', html)
        self.assertIn('aria-label="WhatsApp"', html)

    def test_mobile_contact_ui_exists(self):
        html = self.page()
        self.assertIn('class="menu-toggle"', html)
        self.assertIn('id="mobile-menu"', html)
        self.assertIn('class="mobile-contact-bar"', html)

    def test_mobile_interactions_exist(self):
        html = self.page()
        self.assertIn("window.scrollY > 24", html)
        self.assertIn("mobileMenu.classList.toggle('is-open')", html)
        self.assertIn("toggle.setAttribute('aria-expanded', String(open))", html)

    def test_contact_icons_use_consistent_icon_pack(self):
        html = self.page()
        self.assertIn('class="bxl bxl-telegram"', html)
        self.assertNotIn('class="bi bi-send-fill"', html)
        self.assertNotIn('class="bi bi-telegram"', html)
        self.assertIn('class="bi bi-whatsapp"', html)
        self.assertIn('class="bi bi-telephone-fill"', html)

    def test_mobile_contact_icons_are_larger(self):
        html = self.page()
        self.assertIn('.mobile-contact-bar .contact-icon { width:52px; height:52px; }', html)
        self.assertIn('.mobile-contact-bar .contact-icon svg { width:23px; height:23px; }', html)

    def test_contact_icons_are_optically_centered(self):
        html = self.page()
        self.assertIn('line-height:0;', html)
        self.assertIn('.contact-icon svg { display:block;', html)
        self.assertIn('.contact-icon .bxl-telegram,', html)
        self.assertIn('.contact-icon .bi-whatsapp,', html)
        self.assertIn('.contact-icon .bi-telephone-fill { transform: translateY(0); }', html)

    def test_tariff_prices_match_client_update(self):
        html = self.page()
        self.assertIn('от 14 000 ₽/м²', html)
        self.assertIn('от 18 000 ₽/м²', html)
        self.assertIn('от 22 000 ₽/м²', html)
        self.assertNotIn('от 11 000 ₽/м²', html)

    def test_footer_social_links_are_configured(self):
        html = self.page()
        self.assertIn('const contactConfig = {', html)
        self.assertIn("telegramUrl: 'https://t.me/damalastroy'", html)
        self.assertIn("whatsappUrl: 'https://wa.me/79181792703'", html)
        self.assertIn("maxUrl: 'https://max.ru/damalastroy'", html)
        self.assertIn('data-contact-link="telegram"', html)
        self.assertIn('data-contact-link="whatsapp"', html)
        self.assertIn('data-contact-link="max"', html)
        self.assertNotIn('<div class="social"><a href="#">Telegram</a><a href="#">WhatsApp</a><a href="#">Max</a></div>', html)

    def test_quote_form_opens_prefilled_whatsapp_message(self):
        html = self.page()
        self.assertIn('id="quote-form"', html)
        self.assertIn('name="clientName"', html)
        self.assertIn('name="clientPhone"', html)
        self.assertIn('name="tariff"', html)
        self.assertIn('name="details"', html)
        self.assertIn('type="submit"', html)
        self.assertIn('function buildWhatsAppLeadUrl(form)', html)
        self.assertIn('new FormData(form)', html)
        self.assertIn('encodeURIComponent(message)', html)
        self.assertIn("quoteForm.addEventListener('submit'", html)
        self.assertIn("window.open(buildWhatsAppLeadUrl(quoteForm), '_blank', 'noopener')", html)

    def test_mobile_footer_social_links_wrap_without_overflow(self):
        html = self.page()
        self.assertIn('@media (max-width: 560px)', html)
        self.assertIn('.footer-grid { flex-direction: column; align-items: flex-start; }', html)
        self.assertIn('.social { flex-wrap: wrap; width: 100%; }', html)
        self.assertIn('.social a { text-align: center; }', html)

    def test_yandex_webmaster_verification_meta_exists(self):
        html = self.page()
        self.assertIn('<meta name="yandex-verification" content="353904968985aa3f" />', html)

    def test_yandex_metrika_counter_exists(self):
        html = self.page()
        self.assertIn('Yandex.Metrika counter', html)
        self.assertIn('https://mc.yandex.ru/metrika/tag.js?id=109292117', html)
        self.assertIn("ym(109292117, 'init'", html)
        self.assertIn('webvisor:true', html)
        self.assertIn('clickmap:true', html)
        self.assertIn('accurateTrackBounce:true', html)
        self.assertIn('trackLinks:true', html)
        self.assertNotIn('<noscript><div><img src="https://mc.yandex.ru/watch/109292117"', html)

    def test_seo_meta_tags_target_krasnodar_repair_core(self):
        html = self.page()
        self.assertIn('<title>Ремонт квартир под ключ в Краснодаре — цена от 14 000 ₽/м² | DAMALA STROY</title>', html)
        self.assertIn('<meta name="description" content="Ремонт квартир под ключ в Краснодаре: цена от 14 000 ₽/м², смета до старта, договор, гарантия, ремонт с материалами и без предоплаты." />', html)
        self.assertIn('<meta name="keywords" content="ремонт квартир под ключ Краснодар, ремонт квартир Краснодар цена за м2, ремонт квартиры под ключ цена Краснодар, ремонт квартиры с материалами Краснодар, ремонт квартир без предоплаты Краснодар, ремонт квартиры в новостройке Краснодар, капитальный ремонт квартир Краснодар" />', html)
        self.assertIn('<meta name="geo.placename" content="Краснодар" />', html)
        self.assertIn('<link rel="canonical" href="https://damalastroy.ru/" />', html)
        self.assertIn('<meta property="og:title" content="Ремонт квартир под ключ в Краснодаре — DAMALA STROY" />', html)
        self.assertIn('<meta property="og:description" content="Ремонт квартир под ключ в Краснодаре: цена от 14 000 ₽/м², смета до старта, договор, гарантия и работа без предоплаты." />', html)

    def test_visible_seo_headings_keep_design_structure(self):
        html = self.page()
        self.assertIn('<h1>Ремонт квартир<br><span>под ключ</span></h1>', html)
        self.assertIn('<h2>Пакеты ремонта<br>в Краснодаре</h2>', html)
        self.assertIn('<h2>Ремонт квартир<br>и домов</h2>', html)
        self.assertIn('<h2>Ремонт по договору</h2>', html)
        self.assertIn('<h2>Смета ремонта в 3 вариантах</h2>', html)

    def test_local_business_structured_data_exists(self):
        html = self.page()
        match = re.search(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', html, re.S)
        self.assertIsNotNone(match)
        data = json.loads(match.group(1))
        self.assertEqual(data['@context'], 'https://schema.org')
        self.assertEqual(data['@type'], 'HomeAndConstructionBusiness')
        self.assertEqual(data['@id'], 'https://damalastroy.ru/#business')
        self.assertEqual(data['name'], 'DAMALA STROY')
        self.assertEqual(data['telephone'], '+79181792703')
        self.assertEqual(data['address']['addressLocality'], 'Краснодар')
        self.assertIn('Краснодар', data['areaServed'][0]['name'])
        offer_names = {offer['name'] for offer in data['makesOffer']}
        self.assertIn('Ремонт квартир под ключ в Краснодаре', offer_names)
        self.assertIn('Ремонт квартир в новостройке в Краснодаре', offer_names)
        self.assertIn('Капитальный ремонт квартир в Краснодаре', offer_names)





    def test_capital_repair_page_exists_with_competitor_aligned_semantics(self):
        root = HTML.parent
        page_path = root / 'kapitalnyy-remont-kvartir.html'
        self.assertTrue(page_path.exists())
        page = page_path.read_text(encoding='utf-8')
        self.assertIn('<title>Капитальный ремонт квартир в Краснодаре | DAMALA STROY</title>', page)
        self.assertIn('<h1>Капитальный ремонт квартир в Краснодаре</h1>', page)
        self.assertIn('капитальный ремонт квартиры', page)
        self.assertIn('демонтаж', page)
        self.assertIn('электрика', page)
        self.assertIn('сантехника', page)
        self.assertIn('стяжка', page)
        self.assertIn('выравнивание стен', page)
        self.assertIn('чистовая отделка', page)
        self.assertIn('смета до старта', page)
        self.assertIn('без предоплаты', page)
        self.assertIn('гарантия по договору', page)
        self.assertIn('href="/tseny-na-remont-kvartir.html"', page)

    def test_capital_repair_page_structured_data_exists(self):
        page_html = (HTML.parent / 'kapitalnyy-remont-kvartir.html').read_text(encoding='utf-8')
        scripts = re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', page_html, re.S)
        data = [json.loads(script) for script in scripts]
        service = next((item for item in data if item.get('@type') == 'Service'), None)
        self.assertIsNotNone(service)
        self.assertEqual(service['name'], 'Капитальный ремонт квартир в Краснодаре')
        self.assertEqual(service['provider']['@id'], 'https://damalastroy.ru/#business')
        self.assertEqual(service['areaServed']['name'], 'Краснодар')
        self.assertEqual(service['offers']['lowPrice'], 18000)


    def test_design_repair_page_exists_with_high_ticket_core(self):
        root = HTML.parent
        page_path = root / 'dizayn-i-remont-kvartiry.html'
        self.assertTrue(page_path.exists())
        page = page_path.read_text(encoding='utf-8')
        self.assertIn('<title>Дизайн и ремонт квартиры в Краснодаре | DAMALA STROY</title>', page)
        self.assertIn('<h1>Дизайн и ремонт квартиры в Краснодаре</h1>', page)
        self.assertIn('дизайн и ремонт квартиры', page)
        self.assertIn('дизайнерский ремонт квартир', page)
        self.assertIn('ремонт и дизайн квартиры', page)
        self.assertIn('дизайн-проект', page)
        self.assertIn('подбор материалов', page)
        self.assertIn('смета до старта', page)
        self.assertIn('гарантия по договору', page)
        self.assertIn('href="/tseny-na-remont-kvartir.html"', page)

    def test_design_repair_page_structured_data_exists(self):
        page_html = (HTML.parent / 'dizayn-i-remont-kvartiry.html').read_text(encoding='utf-8')
        scripts = re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', page_html, re.S)
        data = [json.loads(script) for script in scripts]
        service = next((item for item in data if item.get('@type') == 'Service'), None)
        self.assertIsNotNone(service)
        self.assertEqual(service['name'], 'Дизайн и ремонт квартиры в Краснодаре')
        self.assertEqual(service['provider']['@id'], 'https://damalastroy.ru/#business')
        self.assertEqual(service['areaServed']['name'], 'Краснодар')
        self.assertEqual(service['offers']['lowPrice'], 22000)

    def test_turnkey_repair_page_exists_with_main_p1_core(self):
        root = HTML.parent
        page_path = root / 'remont-kvartir-pod-klyuch.html'
        self.assertTrue(page_path.exists())
        page = page_path.read_text(encoding='utf-8')
        self.assertIn('<title>Ремонт квартир под ключ в Краснодаре | DAMALA STROY</title>', page)
        self.assertIn('<h1>Ремонт квартир под ключ в Краснодаре</h1>', page)
        self.assertIn('ремонт квартиры под ключ', page)
        self.assertIn('ремонт под ключ', page)
        self.assertIn('ремонт квартир с материалами', page)
        self.assertIn('без предоплаты', page)
        self.assertIn('гарантия по договору', page)
        self.assertIn('смета до старта', page)
        self.assertIn('href="/tseny-na-remont-kvartir.html"', page)

    def test_turnkey_repair_page_structured_data_exists(self):
        page_html = (HTML.parent / 'remont-kvartir-pod-klyuch.html').read_text(encoding='utf-8')
        scripts = re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', page_html, re.S)
        data = [json.loads(script) for script in scripts]
        service = next((item for item in data if item.get('@type') == 'Service'), None)
        self.assertIsNotNone(service)
        self.assertEqual(service['name'], 'Ремонт квартир под ключ в Краснодаре')
        self.assertEqual(service['provider']['@id'], 'https://damalastroy.ru/#business')
        self.assertEqual(service['areaServed']['name'], 'Краснодар')
        self.assertEqual(service['offers']['lowPrice'], 14000)

    def test_main_page_seo_copy_mentions_price_trust_and_no_prepayment(self):
        html = self.page()
        self.assertIn('без предоплаты', html)
        self.assertIn('ремонт с материалами', html)
        self.assertIn('цена за м²', html)
        self.assertIn('гарантия по договору', html)
        self.assertIn('href="/tseny-na-remont-kvartir.html"', html)
        self.assertIn('href="/dizayn-i-remont-kvartiry.html"', html)

    def test_prices_page_exists_with_commercial_seo_core(self):
        root = HTML.parent
        price_path = root / 'tseny-na-remont-kvartir.html'
        self.assertTrue(price_path.exists())
        page = price_path.read_text(encoding='utf-8')
        self.assertIn('<title>Цены на ремонт квартир в Краснодаре — от 14 000 ₽/м² | DAMALA STROY</title>', page)
        self.assertIn('<h1>Цены на ремонт квартир в Краснодаре</h1>', page)
        self.assertIn('ремонт квартир под ключ цена', page)
        self.assertIn('ремонт квартиры под ключ цена за м2', page)
        self.assertIn('без предоплаты', page)
        self.assertIn('ремонт квартиры с материалами', page)
        self.assertIn('гарантия по договору', page)
        self.assertIn('Start', page)
        self.assertIn('Comfort', page)
        self.assertIn('Design', page)

    def test_prices_page_structured_data_exists(self):
        price_html = (HTML.parent / 'tseny-na-remont-kvartir.html').read_text(encoding='utf-8')
        scripts = re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', price_html, re.S)
        data = [json.loads(script) for script in scripts]
        service = next((item for item in data if item.get('@type') == 'Service'), None)
        self.assertIsNotNone(service)
        self.assertEqual(service['name'], 'Цены на ремонт квартир в Краснодаре')
        offers = service['offers']['offers']
        self.assertEqual(len(offers), 3)
        prices = {offer['price'] for offer in offers}
        self.assertEqual(prices, {14000, 18000, 22000})

    def test_seo_faq_is_separate_page_without_main_landing_block(self):
        root = HTML.parent
        html = self.page()
        faq_path = root / 'faq.html'
        self.assertTrue(faq_path.exists())
        self.assertNotIn('<section id="faq">', html)
        self.assertIn('href="/faq.html"', html)

    def test_faq_page_targets_commercial_questions(self):
        faq = (HTML.parent / 'faq.html').read_text(encoding='utf-8')
        self.assertIn('<h1>Вопросы по ремонту квартир в Краснодаре</h1>', faq)
        self.assertIn('Сколько стоит ремонт квартиры под ключ в Краснодаре?', faq)
        self.assertIn('Цена начинается от 14 000 ₽/м²', faq)
        self.assertIn('Делаете ремонт квартир в новостройках?', faq)
        self.assertIn('Можно ли получить смету до начала работ?', faq)
        self.assertIn('Работаете по договору и с гарантией?', faq)
        self.assertIn('Сколько длится ремонт квартиры?', faq)

    def test_faq_page_structured_data_exists(self):
        faq_html = (HTML.parent / 'faq.html').read_text(encoding='utf-8')
        scripts = re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', faq_html, re.S)
        data = [json.loads(script) for script in scripts]
        faq = next((item for item in data if item.get('@type') == 'FAQPage'), None)
        self.assertIsNotNone(faq)
        self.assertEqual(len(faq['mainEntity']), 5)
        questions = {item['name'] for item in faq['mainEntity']}
        self.assertIn('Сколько стоит ремонт квартиры под ключ в Краснодаре?', questions)
        self.assertIn('Делаете ремонт квартир в новостройках?', questions)
        self.assertIn('Работаете по договору и с гарантией?', questions)

    def test_favicon_is_configured(self):
        html = self.page()
        root = HTML.parent
        self.assertIn('<link rel="icon" type="image/svg+xml" href="/favicon.svg?v=20260520" />', html)
        self.assertTrue((root / 'favicon.svg').exists())
        self.assertIn('<svg', (root / 'favicon.svg').read_text(encoding='utf-8'))

    def test_favicon_has_browser_fallbacks(self):
        html = self.page()
        root = HTML.parent
        self.assertIn('<link rel="shortcut icon" href="/favicon.ico?v=20260520" type="image/x-icon" />', html)
        self.assertIn('<link rel="icon" href="/favicon.ico?v=20260520" sizes="any" />', html)
        self.assertIn('<link rel="mask-icon" href="/safari-pinned-tab.svg?v=20260520" color="#d7a85f" />', html)
        self.assertIn('<link rel="apple-touch-icon" href="/apple-touch-icon.png?v=20260520" />', html)
        self.assertTrue((root / 'favicon.ico').exists())
        self.assertTrue((root / 'apple-touch-icon.png').exists())
        self.assertTrue((root / 'safari-pinned-tab.svg').exists())

    def test_favicon_checker_requirements_are_configured(self):
        html = self.page()
        root = HTML.parent
        self.assertIn('<meta name="apple-mobile-web-app-title" content="DAMALA STROY" />', html)
        self.assertIn('<link rel="icon" type="image/png" sizes="96x96" href="/favicon-96x96.png?v=20260520" />', html)
        self.assertIn('<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png?v=20260520" />', html)
        self.assertIn('<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png?v=20260520" />', html)
        self.assertIn('<link rel="manifest" href="/site.webmanifest?v=20260520" />', html)
        for filename in ['favicon-16x16.png', 'favicon-32x32.png', 'favicon-96x96.png', 'android-chrome-192x192.png', 'android-chrome-512x512.png', 'site.webmanifest']:
            self.assertTrue((root / filename).exists(), filename)
        manifest = (root / 'site.webmanifest').read_text(encoding='utf-8')
        self.assertIn('"name": "DAMALA STROY"', manifest)
        self.assertIn('"short_name": "DAMALA"', manifest)
        self.assertIn('"src": "/android-chrome-192x192.png"', manifest)
        self.assertIn('"src": "/android-chrome-512x512.png"', manifest)



    def test_portfolio_copy_is_client_facing_seo_not_internal_explanation(self):
        html = self.page()
        self.assertIn('Ремонт квартир и домов под ключ в Краснодаре', html)
        self.assertIn('ремонт квартир под ключ', html)
        self.assertIn('ремонт домов под ключ', html)
        self.assertIn('ремонт с материалами', html)
        self.assertIn('смета до старта', html)
        self.assertNotIn('Показываем аккуратную отделку', html)
        self.assertNotIn('реальные сценарии', html)

    def test_renovation_images_are_not_over_darkened_or_framed(self):
        html = self.page()
        self.assertIn('linear-gradient(180deg, rgba(0,0,0,.04), rgba(0,0,0,.28))', html)
        self.assertIn('linear-gradient(180deg, rgba(0,0,0,0) 46%, rgba(0,0,0,.72) 100%)', html)
        self.assertNotIn('.photo-main:before', html)
        self.assertNotIn('.work { min-height: 420px; border-radius: 34px; overflow:hidden; border:1px solid var(--white-line);', html)

    def test_main_page_uses_local_renovation_images(self):
        html = self.page()
        root = HTML.parent
        expected_images = [
            '/assets/images/renovation/damala-renovation-living-room.webp',
            '/assets/images/renovation/damala-renovation-kitchen.webp',
            '/assets/images/renovation/damala-renovation-bathroom.webp',
            '/assets/images/renovation/damala-renovation-rough-stage.webp',
        ]
        for image_url in expected_images:
            self.assertIn(image_url, html)
            self.assertTrue((root / image_url.lstrip('/')).exists(), image_url)
            self.assertTrue((root / image_url.lstrip('/').replace('.webp', '.jpg')).exists(), image_url)
        self.assertNotIn('images.unsplash.com', html)

    def test_visible_copy_uses_client_oriented_seo_language(self):
        html = self.page()
        self.assertIn('ремонт квартир под ключ в Краснодаре', html)
        self.assertIn('цена за м² фиксируется', html)
        self.assertIn('ремонт домов под ключ', html)
        self.assertIn('замер, смета, контроль этапов', html)
        self.assertIn('расчёт стоимости ремонта, сроки и варианты отделки', html)
        self.assertNotIn('без сюрпризов', html)
        self.assertNotIn('без хаоса для клиента', html)
        self.assertNotIn('Линейка сделана так', html)
        self.assertNotIn('Вместо перегруженной листовки', html)
        self.assertNotIn('Клиенту важно не только красиво', html)
        self.assertNotIn('Оставьте контакты, площадь и уровень ремонта', html)


    def test_public_pages_do_not_expose_internal_seo_notes(self):
        forbidden_phrases = [
            'Страница закрывает',
            'страница закрывает',
            'Эта страница создана под',
            'коммерческие запросы',
            'основной коммерческий запрос',
            'близкие формулировки',
            'Для каких объектов подходит',
            'Клиент заранее понимает',
            'спокойствия клиента',
        ]
        for filename in [
            'index.html',
            'faq.html',
            'tseny-na-remont-kvartir.html',
            'remont-kvartir-pod-klyuch.html',
            'kapitalnyy-remont-kvartir.html',
            'dizayn-i-remont-kvartiry.html',
        ]:
            with self.subTest(filename=filename):
                page = (HTML.parent / filename).read_text(encoding='utf-8')
                for phrase in forbidden_phrases:
                    self.assertNotIn(phrase, page)

    def test_sitemap_and_robots_are_configured(self):
        root = HTML.parent
        sitemap = root / 'sitemap.xml'
        robots = root / 'robots.txt'
        self.assertTrue(sitemap.exists())
        self.assertTrue(robots.exists())
        sitemap_text = sitemap.read_text(encoding='utf-8')
        self.assertIn('<loc>https://damalastroy.ru/</loc>', sitemap_text)
        self.assertIn('<loc>https://damalastroy.ru/faq.html</loc>', sitemap_text)
        self.assertIn('<loc>https://damalastroy.ru/tseny-na-remont-kvartir.html</loc>', sitemap_text)
        self.assertIn('<loc>https://damalastroy.ru/remont-kvartir-pod-klyuch.html</loc>', sitemap_text)
        self.assertIn('<loc>https://damalastroy.ru/kapitalnyy-remont-kvartir.html</loc>', sitemap_text)
        self.assertIn('<loc>https://damalastroy.ru/dizayn-i-remont-kvartiry.html</loc>', sitemap_text)
        self.assertIn('<lastmod>2026-05-24</lastmod>', sitemap_text)
        self.assertIn('Sitemap: https://damalastroy.ru/sitemap.xml', robots.read_text(encoding='utf-8'))
        self.assertIn('Allow: /', robots.read_text(encoding='utf-8'))

    def test_legal_documents_and_links_exist(self):
        root = HTML.parent
        html = self.page()
        for filename in ['privacy.html', 'consent.html', 'cookies.html']:
            self.assertTrue((root / filename).exists(), filename)
        self.assertIn('ООО «Ркуб»', html)
        self.assertIn('ИНН 0500048522', html)
        self.assertIn('ОГРН 1260500001970', html)
        self.assertIn('href="/privacy.html"', html)
        self.assertIn('href="/consent.html"', html)
        self.assertIn('href="/cookies.html"', html)
        self.assertIn('Не является публичной офертой', html)

    def test_form_requires_personal_data_consent(self):
        html = self.page()
        self.assertIn('name="personalDataConsent"', html)
        self.assertIn('required', html)
        self.assertIn('Я соглашаюсь на обработку персональных данных', html)
        self.assertIn('if (!quoteForm.personalDataConsent.checked)', html)

    def test_yandex_metrika_is_loaded_after_cookie_consent(self):
        html = self.page()
        self.assertIn('id="cookie-banner"', html)
        self.assertIn('loadYandexMetrika()', html)
        self.assertIn("localStorage.getItem('damalaCookieConsent')", html)
        self.assertIn("localStorage.setItem('damalaCookieConsent', value)", html)
        self.assertIn("saveCookieConsent('accepted')", html)
        self.assertIn("saveCookieConsent('declined')", html)
        self.assertNotIn('<noscript><div><img src="https://mc.yandex.ru/watch/109292117"', html)


if __name__ == '__main__':
    unittest.main()
