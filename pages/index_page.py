from playwright.sync_api import Page
import config


class IndexPage:
    def _stape_login_button(self, page: Page):
        return page.get_by_role("button", name="Войти")

    def open_index_page(self, page: Page) -> None:
        page.goto(config.url.DOMAIN)

    def get_text_from_stape_login_button(self, page: Page) -> str:
        return self._stape_login_button(page).text_content()
