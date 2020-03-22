# Terraform::Panos::PanoramaZone

This resource allows you to add/update/delete zones on Panorama for both
templates and template stacks.

This resource has some overlap with the `panos_panorama_zone_entry`
resource.  If you want to use this resource with the other one, then make
sure that your `panos_panorama_zone` spec does not define the
`interfaces` field.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::PanoramaZone",
    "Properties" : {
        "<a href="#enableuserid" title="EnableUserId">EnableUserId</a>" : <i>Boolean</i>,
        "<a href="#excludeacls" title="ExcludeAcls">ExcludeAcls</a>" : <i>[ String, ... ]</i>,
        "<a href="#includeacls" title="IncludeAcls">IncludeAcls</a>" : <i>[ String, ... ]</i>,
        "<a href="#interfaces" title="Interfaces">Interfaces</a>" : <i>[ String, ... ]</i>,
        "<a href="#logsetting" title="LogSetting">LogSetting</a>" : <i>String</i>,
        "<a href="#mode" title="Mode">Mode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#template" title="Template">Template</a>" : <i>String</i>,
        "<a href="#templatestack" title="TemplateStack">TemplateStack</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#zoneprofile" title="ZoneProfile">ZoneProfile</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::PanoramaZone
Properties:
    <a href="#enableuserid" title="EnableUserId">EnableUserId</a>: <i>Boolean</i>
    <a href="#excludeacls" title="ExcludeAcls">ExcludeAcls</a>: <i>
      - String</i>
    <a href="#includeacls" title="IncludeAcls">IncludeAcls</a>: <i>
      - String</i>
    <a href="#interfaces" title="Interfaces">Interfaces</a>: <i>
      - String</i>
    <a href="#logsetting" title="LogSetting">LogSetting</a>: <i>String</i>
    <a href="#mode" title="Mode">Mode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#template" title="Template">Template</a>: <i>String</i>
    <a href="#templatestack" title="TemplateStack">TemplateStack</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#zoneprofile" title="ZoneProfile">ZoneProfile</a>: <i>String</i>
</pre>

## Properties

#### EnableUserId

Boolean to enable user identification.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeAcls

Users from these addresses/subnets will not
be identified.  This can be an address object, an address group, a single
IP address, or an IP address subnet.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeAcls

Users from these addresses/subnets will
be identified.  This can be an address object, an address group, a single
IP address, or an IP address subnet.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interfaces

List of interfaces to associated with this zone.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogSetting

Log setting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mode

The zone's mode.  This can be `layer3`, `layer2`,
`virtual-wire`, `tap`, or `tunnel`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The zone's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

The template name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateStack

The template stack name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

The vsys to put the zone into (default: `vsys1`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneProfile

The zone protection profile.

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

#### Id

Returns the <code>Id</code> value.

