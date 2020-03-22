# Terraform::Alicloud::PvtzZoneAttachment

Provides vpcs bound to Alicloud Private Zone resource.

-> **NOTE:** Terraform will auto bind vpc to a Private Zone while it uses `alicloud_pvtz_zone_attachment` to build a Private Zone and VPC binding resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::PvtzZoneAttachment",
    "Properties" : {
        "<a href="#lang" title="Lang">Lang</a>" : <i>String</i>,
        "<a href="#userclientip" title="UserClientIp">UserClientIp</a>" : <i>String</i>,
        "<a href="#vpcids" title="VpcIds">VpcIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#zoneid" title="ZoneId">ZoneId</a>" : <i>String</i>,
        "<a href="#vpcs" title="Vpcs">Vpcs</a>" : <i>[ <a href="vpcs.md">Vpcs</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::PvtzZoneAttachment
Properties:
    <a href="#lang" title="Lang">Lang</a>: <i>String</i>
    <a href="#userclientip" title="UserClientIp">UserClientIp</a>: <i>String</i>
    <a href="#vpcids" title="VpcIds">VpcIds</a>: <i>
      - String</i>
    <a href="#zoneid" title="ZoneId">ZoneId</a>: <i>String</i>
    <a href="#vpcs" title="Vpcs">Vpcs</a>: <i>
      - <a href="vpcs.md">Vpcs</a></i>
</pre>

## Properties

#### Lang

The language of code.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserClientIp

The user custom IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcIds

The id List of the VPC with the same region, for example:["vpc-1","vpc-2"].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZoneId

The name of the Private Zone Record.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpcs

_Required_: No

_Type_: List of <a href="vpcs.md">Vpcs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

