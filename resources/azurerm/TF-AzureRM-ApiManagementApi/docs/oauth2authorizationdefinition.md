# TF::AzureRM::ApiManagementApi Oauth2AuthorizationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authorizationservername" title="AuthorizationServerName">AuthorizationServerName</a>" : <i>String</i>,
    "<a href="#scope" title="Scope">Scope</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#authorizationservername" title="AuthorizationServerName">AuthorizationServerName</a>: <i>String</i>
<a href="#scope" title="Scope">Scope</a>: <i>String</i>
</pre>

## Properties

#### AuthorizationServerName

OAuth authorization server identifier. The name of an [OAuth2 Authorization Server](https://www.terraform.io/docs/providers/azurerm/r/api_management_authorization_server.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Scope

Operations scope.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

