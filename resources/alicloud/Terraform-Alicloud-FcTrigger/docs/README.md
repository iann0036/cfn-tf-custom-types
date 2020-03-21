# Terraform::Alicloud::FcTrigger

Provides an Alicloud Function Compute Trigger resource. Based on trigger, execute your code in response to events in Alibaba Cloud.
 For information about Service and how to use it, see [What is Function Compute](https://www.alibabacloud.com/help/doc-detail/52895.htm).

-> **NOTE:** The resource requires a provider field 'account_id'. [See account_id](https://www.terraform.io/docs/providers/alicloud/index.html#account_id).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::FcTrigger",
    "Properties" : {
        "<a href="#config" title="Config">Config</a>" : <i>String</i>,
        "<a href="#configmns" title="ConfigMns">ConfigMns</a>" : <i>String</i>,
        "<a href="#function" title="Function">Function</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nameprefix" title="NamePrefix">NamePrefix</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#service" title="Service">Service</a>" : <i>String</i>,
        "<a href="#sourcearn" title="SourceArn">SourceArn</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::FcTrigger
Properties:
    <a href="#config" title="Config">Config</a>: <i>String</i>
    <a href="#configmns" title="ConfigMns">ConfigMns</a>: <i>String</i>
    <a href="#function" title="Function">Function</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nameprefix" title="NamePrefix">NamePrefix</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#service" title="Service">Service</a>: <i>String</i>
    <a href="#sourcearn" title="SourceArn">SourceArn</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Config

The config of Function Compute trigger.It is valid when `type` is not "mns_topic".See [Configure triggers and events](https://www.alibabacloud.com/help/doc-detail/70140.htm) for more details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConfigMns

The config of Function Compute trigger when the type is "mns_topic".It is conflict with `config`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Function

The Function Compute function name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Function Compute trigger name. It is the only in one service and is conflict with "name_prefix".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamePrefix

Setting a prefix to get a only trigger name. It is conflict with "name".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

RAM role arn attached to the Function Compute trigger. Role used by the event source to call the function. The value format is "acs:ram::$account-id:role/$role-name". See [Create a trigger](https://www.alibabacloud.com/help/doc-detail/53102.htm) for more details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

The Function Compute service name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceArn

Event source resource address. See [Create a trigger](https://www.alibabacloud.com/help/doc-detail/53102.htm) for more details.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The Type of the trigger. Valid values: ["oss", "log", "timer", "http", "mns_topic", "cdn_events"].

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

#### LastModified

Returns the <code>LastModified</code> value.

#### TriggerId

Returns the <code>TriggerId</code> value.

