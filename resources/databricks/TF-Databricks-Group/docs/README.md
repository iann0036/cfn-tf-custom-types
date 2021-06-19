# TF::Databricks::Group

CloudFormation equivalent of databricks_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Databricks::Group",
    "Properties" : {
        "<a href="#allowclustercreate" title="AllowClusterCreate">AllowClusterCreate</a>" : <i>Boolean</i>,
        "<a href="#allowinstancepoolcreate" title="AllowInstancePoolCreate">AllowInstancePoolCreate</a>" : <i>Boolean</i>,
        "<a href="#allowsqlanalyticsaccess" title="AllowSqlAnalyticsAccess">AllowSqlAnalyticsAccess</a>" : <i>Boolean</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Databricks::Group
Properties:
    <a href="#allowclustercreate" title="AllowClusterCreate">AllowClusterCreate</a>: <i>Boolean</i>
    <a href="#allowinstancepoolcreate" title="AllowInstancePoolCreate">AllowInstancePoolCreate</a>: <i>Boolean</i>
    <a href="#allowsqlanalyticsaccess" title="AllowSqlAnalyticsAccess">AllowSqlAnalyticsAccess</a>: <i>Boolean</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
</pre>

## Properties

#### AllowClusterCreate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowInstancePoolCreate

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowSqlAnalyticsAccess

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

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

#### Url

Returns the <code>Url</code> value.

