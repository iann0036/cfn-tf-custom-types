# TF::AWS::DbProxyTarget

Provides an RDS DB proxy target resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::DbProxyTarget",
    "Properties" : {
        "<a href="#dbclusteridentifier" title="DbClusterIdentifier">DbClusterIdentifier</a>" : <i>String</i>,
        "<a href="#dbinstanceidentifier" title="DbInstanceIdentifier">DbInstanceIdentifier</a>" : <i>String</i>,
        "<a href="#dbproxyname" title="DbProxyName">DbProxyName</a>" : <i>String</i>,
        "<a href="#targetgroupname" title="TargetGroupName">TargetGroupName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::DbProxyTarget
Properties:
    <a href="#dbclusteridentifier" title="DbClusterIdentifier">DbClusterIdentifier</a>: <i>String</i>
    <a href="#dbinstanceidentifier" title="DbInstanceIdentifier">DbInstanceIdentifier</a>: <i>String</i>
    <a href="#dbproxyname" title="DbProxyName">DbProxyName</a>: <i>String</i>
    <a href="#targetgroupname" title="TargetGroupName">TargetGroupName</a>: <i>String</i>
</pre>

## Properties

#### DbClusterIdentifier

DB cluster identifier.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbInstanceIdentifier

DB instance identifier.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DbProxyName

The name of the DB proxy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetGroupName

The name of the target group.

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

#### Endpoint

Returns the <code>Endpoint</code> value.

#### Id

Returns the <code>Id</code> value.

#### Port

Returns the <code>Port</code> value.

#### RdsResourceId

Returns the <code>RdsResourceId</code> value.

#### TargetArn

Returns the <code>TargetArn</code> value.

#### TrackedClusterId

Returns the <code>TrackedClusterId</code> value.

#### Type

Returns the <code>Type</code> value.

