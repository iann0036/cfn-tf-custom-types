# TF::AzureRM::DataFactoryIntegrationRuntimeManaged CatalogInfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#administratorlogin" title="AdministratorLogin">AdministratorLogin</a>" : <i>String</i>,
    "<a href="#administratorpassword" title="AdministratorPassword">AdministratorPassword</a>" : <i>String</i>,
    "<a href="#pricingtier" title="PricingTier">PricingTier</a>" : <i>String</i>,
    "<a href="#serverendpoint" title="ServerEndpoint">ServerEndpoint</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#administratorlogin" title="AdministratorLogin">AdministratorLogin</a>: <i>String</i>
<a href="#administratorpassword" title="AdministratorPassword">AdministratorPassword</a>: <i>String</i>
<a href="#pricingtier" title="PricingTier">PricingTier</a>: <i>String</i>
<a href="#serverendpoint" title="ServerEndpoint">ServerEndpoint</a>: <i>String</i>
</pre>

## Properties

#### AdministratorLogin

Administrator login name for the SQL Server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdministratorPassword

Administrator login password for the SQL Server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PricingTier

Pricing tier for the database that will be created for the SSIS catalog. Valid values are: `Basic`, `Standard`, `Premium` and `PremiumRS`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerEndpoint

The endpoint of an Azure SQL Server that will be used to host the SSIS catalog.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

