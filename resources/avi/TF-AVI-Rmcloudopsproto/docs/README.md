# TF::AVI::Rmcloudopsproto

The RmCloudOpsProto resource allows the creation and management of Avi RmCloudOpsProto

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Rmcloudopsproto",
    "Properties" : {
        "<a href="#lastqueriedsecreationlimit" title="LastQueriedSeCreationLimit">LastQueriedSeCreationLimit</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#pendingsecreationcount" title="PendingSeCreationCount">PendingSeCreationCount</a>" : <i>Double</i>,
        "<a href="#pendingvnicopcount" title="PendingVnicOpCount">PendingVnicOpCount</a>" : <i>Double</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Rmcloudopsproto
Properties:
    <a href="#lastqueriedsecreationlimit" title="LastQueriedSeCreationLimit">LastQueriedSeCreationLimit</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#pendingsecreationcount" title="PendingSeCreationCount">PendingSeCreationCount</a>: <i>Double</i>
    <a href="#pendingvnicopcount" title="PendingVnicOpCount">PendingVnicOpCount</a>: <i>Double</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
</pre>

## Properties

#### LastQueriedSeCreationLimit

The most recent value of concurrent se creation limit from cloudconnectorstatus. Field introduced in 20.1.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Cloud name. Field introduced in 20.1.1.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PendingSeCreationCount

Number of se creations in progress. Field introduced in 20.1.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PendingVnicOpCount

Number of vnic operations in progress (both add and delete). Field introduced in 20.1.1.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

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

