# TF::Alicloud::DmsEnterpriseUser

Provides a DMS Enterprise User resource. For information about Alidms Enterprise User and how to use it, see [What is Resource Alidms Enterprise User](https://www.alibabacloud.com/help/doc-detail/98001.htm).

-> **NOTE:** Available in 1.90.0+.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::DmsEnterpriseUser",
    "Properties" : {
        "<a href="#maxexecutecount" title="MaxExecuteCount">MaxExecuteCount</a>" : <i>Double</i>,
        "<a href="#maxresultcount" title="MaxResultCount">MaxResultCount</a>" : <i>Double</i>,
        "<a href="#mobile" title="Mobile">Mobile</a>" : <i>String</i>,
        "<a href="#nickname" title="NickName">NickName</a>" : <i>String</i>,
        "<a href="#rolenames" title="RoleNames">RoleNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#tid" title="Tid">Tid</a>" : <i>Double</i>,
        "<a href="#uid" title="Uid">Uid</a>" : <i>String</i>,
        "<a href="#username" title="UserName">UserName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::DmsEnterpriseUser
Properties:
    <a href="#maxexecutecount" title="MaxExecuteCount">MaxExecuteCount</a>: <i>Double</i>
    <a href="#maxresultcount" title="MaxResultCount">MaxResultCount</a>: <i>Double</i>
    <a href="#mobile" title="Mobile">Mobile</a>: <i>String</i>
    <a href="#nickname" title="NickName">NickName</a>: <i>String</i>
    <a href="#rolenames" title="RoleNames">RoleNames</a>: <i>
      - String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#tid" title="Tid">Tid</a>: <i>Double</i>
    <a href="#uid" title="Uid">Uid</a>: <i>String</i>
    <a href="#username" title="UserName">UserName</a>: <i>String</i>
</pre>

## Properties

#### MaxExecuteCount

Maximum number of inquiries on the day.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxResultCount

Query the maximum number of rows on the day.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mobile

The DingTalk number or mobile number of the user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NickName

The nickname of the user.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleNames

The roles that the user plays.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The state of DMS Enterprise User. Valid values: `NORMAL`, `DISABLE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tid

The tenant ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uid

The Alibaba Cloud unique ID (UID) of the user to add.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserName

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

