# TF::Alkira::ServicePan

CloudFormation equivalent of alkira_service_pan

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alkira::ServicePan",
    "Properties" : {
        "<a href="#billingtags" title="BillingTags">BillingTags</a>" : <i>[ Double, ... ]</i>,
        "<a href="#credentialid" title="CredentialId">CredentialId</a>" : <i>String</i>,
        "<a href="#cxp" title="Cxp">Cxp</a>" : <i>String</i>,
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#licensetype" title="LicenseType">LicenseType</a>" : <i>String</i>,
        "<a href="#managementsegment" title="ManagementSegment">ManagementSegment</a>" : <i>String</i>,
        "<a href="#maxinstancecount" title="MaxInstanceCount">MaxInstanceCount</a>" : <i>Double</i>,
        "<a href="#mininstancecount" title="MinInstanceCount">MinInstanceCount</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#panoramadevicegroup" title="PanoramaDeviceGroup">PanoramaDeviceGroup</a>" : <i>String</i>,
        "<a href="#panoramaenabled" title="PanoramaEnabled">PanoramaEnabled</a>" : <i>String</i>,
        "<a href="#panoramaipaddress" title="PanoramaIpAddress">PanoramaIpAddress</a>" : <i>String</i>,
        "<a href="#panoramatemplate" title="PanoramaTemplate">PanoramaTemplate</a>" : <i>String</i>,
        "<a href="#segments" title="Segments">Segments</a>" : <i>[ String, ... ]</i>,
        "<a href="#size" title="Size">Size</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#instance" title="Instance">Instance</a>" : <i>[ <a href="instancedefinition.md">InstanceDefinition</a>, ... ]</i>,
        "<a href="#zonestogroups" title="ZonesToGroups">ZonesToGroups</a>" : <i>[ <a href="zonestogroupsdefinition.md">ZonesToGroupsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alkira::ServicePan
Properties:
    <a href="#billingtags" title="BillingTags">BillingTags</a>: <i>
      - Double</i>
    <a href="#credentialid" title="CredentialId">CredentialId</a>: <i>String</i>
    <a href="#cxp" title="Cxp">Cxp</a>: <i>String</i>
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#licensetype" title="LicenseType">LicenseType</a>: <i>String</i>
    <a href="#managementsegment" title="ManagementSegment">ManagementSegment</a>: <i>String</i>
    <a href="#maxinstancecount" title="MaxInstanceCount">MaxInstanceCount</a>: <i>Double</i>
    <a href="#mininstancecount" title="MinInstanceCount">MinInstanceCount</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#panoramadevicegroup" title="PanoramaDeviceGroup">PanoramaDeviceGroup</a>: <i>String</i>
    <a href="#panoramaenabled" title="PanoramaEnabled">PanoramaEnabled</a>: <i>String</i>
    <a href="#panoramaipaddress" title="PanoramaIpAddress">PanoramaIpAddress</a>: <i>String</i>
    <a href="#panoramatemplate" title="PanoramaTemplate">PanoramaTemplate</a>: <i>String</i>
    <a href="#segments" title="Segments">Segments</a>: <i>
      - String</i>
    <a href="#size" title="Size">Size</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#instance" title="Instance">Instance</a>: <i>
      - <a href="instancedefinition.md">InstanceDefinition</a></i>
    <a href="#zonestogroups" title="ZonesToGroups">ZonesToGroups</a>: <i>
      - <a href="zonestogroupsdefinition.md">ZonesToGroupsDefinition</a></i>
</pre>

## Properties

#### BillingTags

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CredentialId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cxp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicenseType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagementSegment

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxInstanceCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinInstanceCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PanoramaDeviceGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PanoramaEnabled

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PanoramaIpAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PanoramaTemplate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Segments

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instance

_Required_: No

_Type_: List of <a href="instancedefinition.md">InstanceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZonesToGroups

_Required_: No

_Type_: List of <a href="zonestogroupsdefinition.md">ZonesToGroupsDefinition</a>

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

#### ServiceId

Returns the <code>ServiceId</code> value.

