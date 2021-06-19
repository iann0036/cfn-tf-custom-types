# TF::SumoLogic::SamlConfiguration

Provides a [Sumologic SAML Configuration][1].

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::SumoLogic::SamlConfiguration",
    "Properties" : {
        "<a href="#authnrequesturl" title="AuthnRequestUrl">AuthnRequestUrl</a>" : <i>String</i>,
        "<a href="#configurationname" title="ConfigurationName">ConfigurationName</a>" : <i>String</i>,
        "<a href="#debugmode" title="DebugMode">DebugMode</a>" : <i>Boolean</i>,
        "<a href="#disablerequestedauthncontext" title="DisableRequestedAuthnContext">DisableRequestedAuthnContext</a>" : <i>Boolean</i>,
        "<a href="#emailattribute" title="EmailAttribute">EmailAttribute</a>" : <i>String</i>,
        "<a href="#isredirectbinding" title="IsRedirectBinding">IsRedirectBinding</a>" : <i>Boolean</i>,
        "<a href="#issuer" title="Issuer">Issuer</a>" : <i>String</i>,
        "<a href="#logoutenabled" title="LogoutEnabled">LogoutEnabled</a>" : <i>Boolean</i>,
        "<a href="#logouturl" title="LogoutUrl">LogoutUrl</a>" : <i>String</i>,
        "<a href="#rolesattribute" title="RolesAttribute">RolesAttribute</a>" : <i>String</i>,
        "<a href="#signauthnrequest" title="SignAuthnRequest">SignAuthnRequest</a>" : <i>Boolean</i>,
        "<a href="#spinitiatedloginenabled" title="SpInitiatedLoginEnabled">SpInitiatedLoginEnabled</a>" : <i>Boolean</i>,
        "<a href="#spinitiatedloginpath" title="SpInitiatedLoginPath">SpInitiatedLoginPath</a>" : <i>String</i>,
        "<a href="#x509cert1" title="X509cert1">X509cert1</a>" : <i>String</i>,
        "<a href="#x509cert2" title="X509cert2">X509cert2</a>" : <i>String</i>,
        "<a href="#x509cert3" title="X509cert3">X509cert3</a>" : <i>String</i>,
        "<a href="#ondemandprovisioningenabled" title="OnDemandProvisioningEnabled">OnDemandProvisioningEnabled</a>" : <i>[ <a href="ondemandprovisioningenableddefinition.md">OnDemandProvisioningEnabledDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::SumoLogic::SamlConfiguration
Properties:
    <a href="#authnrequesturl" title="AuthnRequestUrl">AuthnRequestUrl</a>: <i>String</i>
    <a href="#configurationname" title="ConfigurationName">ConfigurationName</a>: <i>String</i>
    <a href="#debugmode" title="DebugMode">DebugMode</a>: <i>Boolean</i>
    <a href="#disablerequestedauthncontext" title="DisableRequestedAuthnContext">DisableRequestedAuthnContext</a>: <i>Boolean</i>
    <a href="#emailattribute" title="EmailAttribute">EmailAttribute</a>: <i>String</i>
    <a href="#isredirectbinding" title="IsRedirectBinding">IsRedirectBinding</a>: <i>Boolean</i>
    <a href="#issuer" title="Issuer">Issuer</a>: <i>String</i>
    <a href="#logoutenabled" title="LogoutEnabled">LogoutEnabled</a>: <i>Boolean</i>
    <a href="#logouturl" title="LogoutUrl">LogoutUrl</a>: <i>String</i>
    <a href="#rolesattribute" title="RolesAttribute">RolesAttribute</a>: <i>String</i>
    <a href="#signauthnrequest" title="SignAuthnRequest">SignAuthnRequest</a>: <i>Boolean</i>
    <a href="#spinitiatedloginenabled" title="SpInitiatedLoginEnabled">SpInitiatedLoginEnabled</a>: <i>Boolean</i>
    <a href="#spinitiatedloginpath" title="SpInitiatedLoginPath">SpInitiatedLoginPath</a>: <i>String</i>
    <a href="#x509cert1" title="X509cert1">X509cert1</a>: <i>String</i>
    <a href="#x509cert2" title="X509cert2">X509cert2</a>: <i>String</i>
    <a href="#x509cert3" title="X509cert3">X509cert3</a>: <i>String</i>
    <a href="#ondemandprovisioningenabled" title="OnDemandProvisioningEnabled">OnDemandProvisioningEnabled</a>: <i>
      - <a href="ondemandprovisioningenableddefinition.md">OnDemandProvisioningEnabledDefinition</a></i>
</pre>

## Properties

#### AuthnRequestUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigurationName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DebugMode

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableRequestedAuthnContext

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EmailAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsRedirectBinding

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Issuer

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogoutEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogoutUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RolesAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SignAuthnRequest

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpInitiatedLoginEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpInitiatedLoginPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### X509cert1

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### X509cert2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### X509cert3

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnDemandProvisioningEnabled

_Required_: No

_Type_: List of <a href="ondemandprovisioningenableddefinition.md">OnDemandProvisioningEnabledDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Certificate

Returns the <code>Certificate</code> value.

#### Id

Returns the <code>Id</code> value.

