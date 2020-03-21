# Terraform::AzureRM::ApiManagementAuthorizationServer

Manages an Authorization Server within an API Management Service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureRM::ApiManagementAuthorizationServer",
    "Properties" : {
        "<a href="#apimanagementname" title="ApiManagementName">ApiManagementName</a>" : <i>String</i>,
        "<a href="#authorizationendpoint" title="AuthorizationEndpoint">AuthorizationEndpoint</a>" : <i>String</i>,
        "<a href="#authorizationmethods" title="AuthorizationMethods">AuthorizationMethods</a>" : <i>[ String, ... ]</i>,
        "<a href="#bearertokensendingmethods" title="BearerTokenSendingMethods">BearerTokenSendingMethods</a>" : <i>[ String, ... ]</i>,
        "<a href="#clientauthenticationmethod" title="ClientAuthenticationMethod">ClientAuthenticationMethod</a>" : <i>[ String, ... ]</i>,
        "<a href="#clientid" title="ClientId">ClientId</a>" : <i>String</i>,
        "<a href="#clientregistrationendpoint" title="ClientRegistrationEndpoint">ClientRegistrationEndpoint</a>" : <i>String</i>,
        "<a href="#clientsecret" title="ClientSecret">ClientSecret</a>" : <i>String</i>,
        "<a href="#defaultscope" title="DefaultScope">DefaultScope</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#granttypes" title="GrantTypes">GrantTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>" : <i>String</i>,
        "<a href="#resourceownerpassword" title="ResourceOwnerPassword">ResourceOwnerPassword</a>" : <i>String</i>,
        "<a href="#resourceownerusername" title="ResourceOwnerUsername">ResourceOwnerUsername</a>" : <i>String</i>,
        "<a href="#supportstate" title="SupportState">SupportState</a>" : <i>Boolean</i>,
        "<a href="#tokenendpoint" title="TokenEndpoint">TokenEndpoint</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#tokenbodyparameter" title="TokenBodyParameter">TokenBodyParameter</a>" : <i>[ <a href="tokenbodyparameter.md">TokenBodyParameter</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureRM::ApiManagementAuthorizationServer
Properties:
    <a href="#apimanagementname" title="ApiManagementName">ApiManagementName</a>: <i>String</i>
    <a href="#authorizationendpoint" title="AuthorizationEndpoint">AuthorizationEndpoint</a>: <i>String</i>
    <a href="#authorizationmethods" title="AuthorizationMethods">AuthorizationMethods</a>: <i>
      - String</i>
    <a href="#bearertokensendingmethods" title="BearerTokenSendingMethods">BearerTokenSendingMethods</a>: <i>
      - String</i>
    <a href="#clientauthenticationmethod" title="ClientAuthenticationMethod">ClientAuthenticationMethod</a>: <i>
      - String</i>
    <a href="#clientid" title="ClientId">ClientId</a>: <i>String</i>
    <a href="#clientregistrationendpoint" title="ClientRegistrationEndpoint">ClientRegistrationEndpoint</a>: <i>String</i>
    <a href="#clientsecret" title="ClientSecret">ClientSecret</a>: <i>String</i>
    <a href="#defaultscope" title="DefaultScope">DefaultScope</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#granttypes" title="GrantTypes">GrantTypes</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#resourcegroupname" title="ResourceGroupName">ResourceGroupName</a>: <i>String</i>
    <a href="#resourceownerpassword" title="ResourceOwnerPassword">ResourceOwnerPassword</a>: <i>String</i>
    <a href="#resourceownerusername" title="ResourceOwnerUsername">ResourceOwnerUsername</a>: <i>String</i>
    <a href="#supportstate" title="SupportState">SupportState</a>: <i>Boolean</i>
    <a href="#tokenendpoint" title="TokenEndpoint">TokenEndpoint</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#tokenbodyparameter" title="TokenBodyParameter">TokenBodyParameter</a>: <i>
      - <a href="tokenbodyparameter.md">TokenBodyParameter</a></i>
</pre>

## Properties

#### ApiManagementName

The name of the API Management Service in which this Authorization Server should be created. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizationEndpoint

The OAUTH Authorization Endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthorizationMethods

The HTTP Verbs supported by the Authorization Endpoint. Possible values are `DELETE`, `GET`, `HEAD`, `OPTIONS`, `PATCH`, `POST`, `PUT` and `TRACE`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BearerTokenSendingMethods

The mechanism by which Access Tokens are passed to the API. Possible values are `authorizationHeader` and `query`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientAuthenticationMethod

The Authentication Methods supported by the Token endpoint of this Authorization Server.. Possible values are `Basic` and `Body`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientId

The Client/App ID registered with this Authorization Server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientRegistrationEndpoint

The URI of page where Client/App Registration is performed for this Authorization Server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientSecret

The Client/App Secret registered with this Authorization Server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultScope

The Default Scope used when requesting an Access Token, specified as a string containing space-delimited values.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the Authorization Server, which may contain HTML formatting tags.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The user-friendly name of this Authorization Server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GrantTypes

Form of Authorization Grants required when requesting an Access Token. Possible values are `authorizationCode`, `clientCredentials`, `implicit` and `resourceOwnerPassword`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Name of the Parameter.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupName

The name of the Resource Group in which the API Management Service exists. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceOwnerPassword

The password associated with the Resource Owner.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceOwnerUsername

The username associated with the Resource Owner.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SupportState

Does this Authorization Server support State? If this is set to `true` the client may use the state parameter to raise protocol security.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenEndpoint

The OAUTH Token Endpoint.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenBodyParameter

_Required_: No

_Type_: List of <a href="tokenbodyparameter.md">TokenBodyParameter</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

