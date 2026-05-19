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
        self.assertIn('<meta name="description" content="Ремонт квартир и домов под ключ в Краснодаре от DAMALA STROY: фиксированная смета, договор, гарантия, замер и клининг. Цены от 14 000 ₽/м²." />', html)
        self.assertIn('<meta name="keywords" content="ремонт квартир под ключ Краснодар, ремонт под ключ Краснодар, ремонт квартир Краснодар цена за м2, ремонт квартиры в новостройке Краснодар, дизайнерский ремонт квартиры Краснодар, косметический ремонт Краснодар, капитальный ремонт квартиры Краснодар" />', html)
        self.assertIn('<meta name="geo.placename" content="Краснодар" />', html)
        self.assertIn('<link rel="canonical" href="https://damalastroy.ru/" />', html)
        self.assertIn('<meta property="og:title" content="Ремонт квартир под ключ в Краснодаре — DAMALA STROY" />', html)
        self.assertIn('<meta property="og:description" content="Ремонт квартир и домов под ключ в Краснодаре: фиксированная смета, договор, гарантия, замер и клининг. Цены от 14 000 ₽/м²." />', html)

    def test_favicon_is_configured(self):
        html = self.page()
        root = HTML.parent
        self.assertIn('<link rel="icon" type="image/svg+xml" href="/favicon.svg" />', html)
        self.assertTrue((root / 'favicon.svg').exists())
        self.assertIn('<svg', (root / 'favicon.svg').read_text(encoding='utf-8'))

    def test_visible_copy_uses_client_oriented_seo_language(self):
        html = self.page()
        self.assertIn('ремонт квартир под ключ в Краснодаре', html)
        self.assertIn('понятной ценой за м²', html)
        self.assertIn('дом под ключ в Краснодаре', html)
        self.assertIn('замер, смета, договор, контроль работ', html)
        self.assertIn('расчёт стоимости, сроки и варианты отделки', html)
        self.assertNotIn('без хаоса для клиента', html)
        self.assertNotIn('Линейка сделана так', html)
        self.assertNotIn('Вместо перегруженной листовки', html)
        self.assertNotIn('Клиенту важно не только красиво', html)
        self.assertNotIn('Оставьте контакты, площадь и уровень ремонта', html)

    def test_sitemap_and_robots_are_configured(self):
        root = HTML.parent
        sitemap = root / 'sitemap.xml'
        robots = root / 'robots.txt'
        self.assertTrue(sitemap.exists())
        self.assertTrue(robots.exists())
        self.assertIn('<loc>https://damalastroy.ru/</loc>', sitemap.read_text(encoding='utf-8'))
        self.assertIn('<lastmod>2026-05-19</lastmod>', sitemap.read_text(encoding='utf-8'))
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
