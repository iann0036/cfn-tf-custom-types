# TF::AzureRM::ApiManagementApi OpenidAuthenticationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#bearertokensendingmethods" title="BearerTokenSendingMethods">BearerTokenSendingMethods</a>" : <i>[ String, ... ]</i>,
    "<a href="#openidprovidername" title="OpenidProviderName">OpenidProviderName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#bearertokensendingmethods" title="BearerTokenSendingMethods">BearerTokenSendingMethods</a>: <i>
      - String</i>
<a href="#openidprovidername" title="OpenidProviderName">OpenidProviderName</a>: <i>String</i>
</pre>

## Properties

#### BearerTokenSendingMethods

How to send token to the server. A list of zero or more methods. Valid values are `authorizationHeader` and `query`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenidProviderName

OpenID Connect provider identifier. The name of an [OpenID Connect Provider](https://www.terraform.io/docs/providers/azurerm/r/api_management_openid_connect_provider.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

