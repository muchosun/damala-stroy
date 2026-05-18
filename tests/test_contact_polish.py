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


if __name__ == '__main__':
    unittest.main()
