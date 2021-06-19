# TF::OneLogin::Apps

Creates a Basic Application.

This resource allows you to create and configure a Basic (non-SAML non-OIDC) Application.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OneLogin::Apps",
    "Properties" : {
        "<a href="#allowassumedsignin" title="AllowAssumedSignin">AllowAssumedSignin</a>" : <i>Boolean</i>,
        "<a href="#brandid" title="BrandId">BrandId</a>" : <i>Double</i>,
        "<a href="#connectorid" title="ConnectorId">ConnectorId</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#provisioning" title="Provisioning">Provisioning</a>" : <i>[ <a href="provisioningdefinition.md">ProvisioningDefinition</a>, ... ]</i>,
        "<a href="#visible" title="Visible">Visible</a>" : <i>Boolean</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parametersdefinition.md">ParametersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OneLogin::Apps
Properties:
    <a href="#allowassumedsignin" title="AllowAssumedSignin">AllowAssumedSignin</a>: <i>Boolean</i>
    <a href="#brandid" title="BrandId">BrandId</a>: <i>Double</i>
    <a href="#connectorid" title="ConnectorId">ConnectorId</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#provisioning" title="Provisioning">Provisioning</a>: <i>
      - <a href="provisioningdefinition.md">ProvisioningDefinition</a></i>
    <a href="#visible" title="Visible">Visible</a>: <i>Boolean</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parametersdefinition.md">ParametersDefinition</a></i>
</pre>

## Properties

#### AllowAssumedSignin

Enable sign in when user has been assumed by the account owner. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BrandId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectorId

The ID for the app connector, dictates the type of app (e.g. AWS Multi-Role App).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

App description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The app's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

Notes about the app.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Provisioning

Settings regarding the app's provisioning ability.
* `enabled` - (Required) Indicates if provisioning is enabled for this app.

_Required_: No

_Type_: List of <a href="provisioningdefinition.md">ProvisioningDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visible

Determine if app should be visible in OneLogin portal. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

_Required_: No

_Type_: List of <a href="parametersdefinition.md">ParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AuthMethod

Returns the <code>AuthMethod</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### IconUrl

Returns the <code>IconUrl</code> value.

#### Id

Returns the <code>Id</code> value.

#### PolicyId

Returns the <code>PolicyId</code> value.

#### TabId

Returns the <code>TabId</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.

