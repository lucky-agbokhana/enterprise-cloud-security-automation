provider "azurerm" {

  features {}
}

resource "azurerm_resource_group" "security_lab" {
  name     = "rg-security-audit-lab"
  location = "eastus"
}

resource "azurerm_storage_account" "insecure_storage" {
  name                     = "insecurelab${random_id.suffix.hex}"
  resource_group_name      = azurerm_resource_group.security_lab.name
  location                 = azurerm_resource_group.security_lab.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  # SECURITY VULNERABILITY:
  public_network_access_enabled = false
  allow_nested_items_to_be_public = false
  min_tls_version = "TLS1_2"
}

resource "random_id" "suffix" {
  byte_length = 4
}