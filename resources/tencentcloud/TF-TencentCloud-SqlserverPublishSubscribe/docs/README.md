# TF::TencentCloud::SqlserverPublishSubscribe

Provides a SQL Server PublishSubscribe resource belongs to SQL Server instance.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::SqlserverPublishSubscribe",
    "Properties" : {
        "<a href="#deletesubscribedb" title="DeleteSubscribeDb">DeleteSubscribeDb</a>" : <i>Boolean</i>,
        "<a href="#publishinstanceid" title="PublishInstanceId">PublishInstanceId</a>" : <i>String</i>,
        "<a href="#publishsubscribename" title="PublishSubscribeName">PublishSubscribeName</a>" : <i>String</i>,
        "<a href="#subscribeinstanceid" title="SubscribeInstanceId">SubscribeInstanceId</a>" : <i>String</i>,
        "<a href="#databasetuples" title="DatabaseTuples">DatabaseTuples</a>" : <i>[ <a href="databasetuplesdefinition.md">DatabaseTuplesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::SqlserverPublishSubscribe
Properties:
    <a href="#deletesubscribedb" title="DeleteSubscribeDb">DeleteSubscribeDb</a>: <i>Boolean</i>
    <a href="#publishinstanceid" title="PublishInstanceId">PublishInstanceId</a>: <i>String</i>
    <a href="#publishsubscribename" title="PublishSubscribeName">PublishSubscribeName</a>: <i>String</i>
    <a href="#subscribeinstanceid" title="SubscribeInstanceId">SubscribeInstanceId</a>: <i>String</i>
    <a href="#databasetuples" title="DatabaseTuples">DatabaseTuples</a>: <i>
      - <a href="databasetuplesdefinition.md">DatabaseTuplesDefinition</a></i>
</pre>

## Properties

#### DeleteSubscribeDb

Whether to delete the subscriber database when deleting the Publish and Subscribe. `true` for deletes the subscribe database, `false` for does not delete the subscribe database. default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishInstanceId

ID of the SQL Server instance which publish.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishSubscribeName

The name of the Publish and Subscribe. Default is `default_name`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubscribeInstanceId

ID of the SQL Server instance which subscribe.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DatabaseTuples

_Required_: No

_Type_: List of <a href="databasetuplesdefinition.md">DatabaseTuplesDefinition</a>

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

