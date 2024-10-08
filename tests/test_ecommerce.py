from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class TestEcommerceWebsite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox() 
        cls.driver.maximize_window()
        cls.base_path = "file:///home/kratos/coding_files/projects/st_project/ecommerce/"
    
    def handle_alert(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.dismiss()
            print("Alert dismissed")
        except Exception as e:
            print(f"No alert present or alert handling failed: {e}")
    
    def test_home_page_title(self):
        self.driver.get(self.base_path + 'index.html')
        WebDriverWait(self.driver, 20).until(EC.title_contains("E-commerce Website"))
        self.assertIn("E-commerce Website", self.driver.title)
    
    def test_product_list_page(self):
        self.driver.get(self.base_path + 'product-list.html')
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product")))
        products = self.driver.find_elements(By.CLASS_NAME, "product")
        self.assertGreater(len(products), 0)
    
    def test_product_detail_page(self):
        self.driver.get(self.base_path + 'product-detail.html')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
        product_name = self.driver.find_element(By.TAG_NAME, "h3")
        self.assertIn("Product 1", product_name.text)
    
    def test_add_to_cart(self):
        self.driver.get(self.base_path + 'product-detail.html')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "add-to-cart"))).click()
        time.sleep(1)  
        self.handle_alert()  
        self.driver.get(self.base_path + 'cart.html')
        self.handle_alert() 
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "cart-item")))
        cart_items = self.driver.find_elements(By.CLASS_NAME, "cart-item")
        self.assertGreater(len(cart_items), 0)
    
    def test_cart_page(self):
        self.driver.get(self.base_path + 'cart.html')
        WebDriverWait(self.driver, 20).until(EC.title_contains("Cart"))
        self.assertIn("Cart", self.driver.title)
    
    def test_checkout_page(self):
        self.driver.get(self.base_path + 'checkout.html')
        WebDriverWait(self.driver, 20).until(EC.title_contains("Checkout"))
        self.assertIn("Checkout", self.driver.title)
    
    def test_checkout_form(self):
        self.driver.get(self.base_path + 'checkout.html')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "name")))
        name_field = self.driver.find_element(By.ID, "name")
        address_field = self.driver.find_element(By.ID, "address")
        submit_button = self.driver.find_element(By.TAG_NAME, "button")
        name_field.send_keys("John Doe")
        address_field.send_keys("123 Main St")
        submit_button.click()
        time.sleep(1)  

        try:
            WebDriverWait(self.driver, 20).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()  
            print(f"Alert text: {alert_text}")
            self.assertIn("Order placed successfully!", alert_text)
        except Exception as e:
            self.fail(f"Failed to handle alert: {e}")
    
    def test_navigation_links(self):
        self.driver.get(self.base_path + 'index.html')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Home")))
        home_link = self.driver.find_element(By.LINK_TEXT, "Home")
        products_link = self.driver.find_element(By.LINK_TEXT, "Products")
        cart_link = self.driver.find_element(By.LINK_TEXT, "Cart")
        self.assertTrue(home_link.is_displayed())
        self.assertTrue(products_link.is_displayed())
        self.assertTrue(cart_link.is_displayed())
    
    def test_featured_products_display(self):
        self.driver.get(self.base_path + 'index.html')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "featured-products")))
        featured_products = self.driver.find_elements(By.ID, "featured-products")
        self.assertGreater(len(featured_products), 0)
    
    def test_product_images(self):
        self.driver.get(self.base_path + 'product-list.html')
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))
        images = self.driver.find_elements(By.TAG_NAME, "img")
        for image in images:
            self.assertTrue(image.is_displayed())
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
