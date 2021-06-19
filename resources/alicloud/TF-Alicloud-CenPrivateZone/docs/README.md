# TF::Alicloud::CenPrivateZone

This topic describes how to configure PrivateZone access. 
PrivateZone is a VPC-based resolution and management service for private domain names. 
After you set a PrivateZone access, the Cloud Connect Network (CCN) and Virtual Border Router (VBR) attached to a CEN instance can access the PrivateZone service through CEN.

For information about CEN Private Zone and how to use it, see [Manage CEN Private Zone](https://www.alibabacloud.com/help/en/doc-detail/106693.htm).

-> **NOTE:** Available in 1.83.0+

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::CenPrivateZone",
    "Properties" : {
        "<a href="#accessregionid" title="AccessRegionId">AccessRegionId</a>" : <i>String</i>,
        "<a href="#cenid" title="CenId">CenId</a>" : <i>String</i>,
        "<a href="#hostregionid" title="HostRegionId">HostRegionId</a>" : <i>String</i>,
        "<a href="#hostvpcid" title="HostVpcId">HostVpcId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::CenPrivateZone
Properties:
    <a href="#accessregionid" title="AccessRegionId">AccessRegionId</a>: <i>String</i>
    <a href="#cenid" title="CenId">CenId</a>: <i>String</i>
    <a href="#hostregionid" title="HostRegionId">HostRegionId</a>: <i>String</i>
    <a href="#hostvpcid" title="HostVpcId">HostVpcId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AccessRegionId

The access region. The access region is the region of the cloud resource that accesses the PrivateZone service through CEN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CenId

The ID of the CEN instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostRegionId

The service region. The service region is the target region of the PrivateZone service to be accessed through CEN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostVpcId

The VPC that belongs to the service region.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### Status

Returns the <code>Status</code> value.

