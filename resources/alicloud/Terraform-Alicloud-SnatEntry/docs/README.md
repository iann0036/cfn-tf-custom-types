# Terraform::Alicloud::SnatEntry

CloudFormation equivalent of alicloud_snat_entry

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::SnatEntry",
    "Properties" : {
        "<a href="#snatentryname" title="SnatEntryName">SnatEntryName</a>" : <i>String</i>,
        "<a href="#snatip" title="SnatIp">SnatIp</a>" : <i>String</i>,
        "<a href="#snattableid" title="SnatTableId">SnatTableId</a>" : <i>String</i>,
        "<a href="#sourcecidr" title="SourceCidr">SourceCidr</a>" : <i>String</i>,
        "<a href="#sourcevswitchid" title="SourceVswitchId">SourceVswitchId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::SnatEntry
Properties:
    <a href="#snatentryname" title="SnatEntryName">SnatEntryName</a>: <i>String</i>
    <a href="#snatip" title="SnatIp">SnatIp</a>: <i>String</i>
    <a href="#snattableid" title="SnatTableId">SnatTableId</a>: <i>String</i>
    <a href="#sourcecidr" title="SourceCidr">SourceCidr</a>: <i>String</i>
    <a href="#sourcevswitchid" title="SourceVswitchId">SourceVswitchId</a>: <i>String</i>
</pre>

## Properties

#### SnatEntryName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatIp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnatTableId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceCidr

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceVswitchId

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

#### SnatEntryId

Returns the <code>SnatEntryId</code> value.

