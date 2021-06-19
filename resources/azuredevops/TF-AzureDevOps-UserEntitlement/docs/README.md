# TF::AzureDevOps::UserEntitlement

Manages a user entitlement within Azure DevOps.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AzureDevOps::UserEntitlement",
    "Properties" : {
        "<a href="#accountlicensetype" title="AccountLicenseType">AccountLicenseType</a>" : <i>String</i>,
        "<a href="#licensingsource" title="LicensingSource">LicensingSource</a>" : <i>String</i>,
        "<a href="#origin" title="Origin">Origin</a>" : <i>String</i>,
        "<a href="#originid" title="OriginId">OriginId</a>" : <i>String</i>,
        "<a href="#principalname" title="PrincipalName">PrincipalName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AzureDevOps::UserEntitlement
Properties:
    <a href="#accountlicensetype" title="AccountLicenseType">AccountLicenseType</a>: <i>String</i>
    <a href="#licensingsource" title="LicensingSource">LicensingSource</a>: <i>String</i>
    <a href="#origin" title="Origin">Origin</a>: <i>String</i>
    <a href="#originid" title="OriginId">OriginId</a>: <i>String</i>
    <a href="#principalname" title="PrincipalName">PrincipalName</a>: <i>String</i>
</pre>

## Properties

#### AccountLicenseType

Type of Account License. Valid values: `advanced`, `earlyAdopter`, `express`, `none`, `professional`, or `stakeholder`. Defaults to `express`. In addition the value `basic` is allowed which is an alias for `express` and reflects the name of the `express` license used in the Azure DevOps web interface.
- `licensing_source` - (Optional) The source of the licensing (e.g. Account. MSDN etc.) Valid values: `account` (Default), `auto`, `msdn`, `none`, `profile`, `trail`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicensingSource

The source of the licensing (e.g. Account. MSDN etc.) Valid values: `account` (Default), `auto`, `msdn`, `none`, `profile`, `trail`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Origin

The type of source provider for the origin identifier.
- `account_license_type` - (Optional) Type of Account License. Valid values: `advanced`, `earlyAdopter`, `express`, `none`, `professional`, or `stakeholder`. Defaults to `express`. In addition the value `basic` is allowed which is an alias for `express` and reflects the name of the `express` license used in the Azure DevOps web interface.
- `licensing_source` - (Optional) The source of the licensing (e.g. Account. MSDN etc.) Valid values: `account` (Default), `auto`, `msdn`, `none`, `profile`, `trail`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OriginId

The unique identifier from the system of origin. Typically a sid, object id or Guid. e.g. Used for member of other tenant on Azure Active Directory.
- `origin` - (Optional) The type of source provider for the origin identifier.
- `account_license_type` - (Optional) Type of Account License. Valid values: `advanced`, `earlyAdopter`, `express`, `none`, `professional`, or `stakeholder`. Defaults to `express`. In addition the value `basic` is allowed which is an alias for `express` and reflects the name of the `express` license used in the Azure DevOps web interface.
- `licensing_source` - (Optional) The source of the licensing (e.g. Account. MSDN etc.) Valid values: `account` (Default), `auto`, `msdn`, `none`, `profile`, `trail`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrincipalName

The principal name is the PrincipalName of a graph member from the source provider. Usually, e-mail address.
- `origin_id` - (Optional) The unique identifier from the system of origin. Typically a sid, object id or Guid. e.g. Used for member of other tenant on Azure Active Directory.
- `origin` - (Optional) The type of source provider for the origin identifier.
- `account_license_type` - (Optional) Type of Account License. Valid values: `advanced`, `earlyAdopter`, `express`, `none`, `professional`, or `stakeholder`. Defaults to `express`. In addition the value `basic` is allowed which is an alias for `express` and reflects the name of the `express` license used in the Azure DevOps web interface.
- `licensing_source` - (Optional) The source of the licensing (e.g. Account. MSDN etc.) Valid values: `account` (Default), `auto`, `msdn`, `none`, `profile`, `trail`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Descriptor

Returns the <code>Descriptor</code> value.

#### Id

Returns the <code>Id</code> value.

