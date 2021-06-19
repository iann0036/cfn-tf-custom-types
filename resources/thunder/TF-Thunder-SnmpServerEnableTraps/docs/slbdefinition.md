# TF::Thunder::SnmpServerEnableTraps SlbDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#all" title="All">All</a>" : <i>Double</i>,
    "<a href="#applicationbufferlimit" title="ApplicationBufferLimit">ApplicationBufferLimit</a>" : <i>Double</i>,
    "<a href="#bwratelimitexceed" title="BwRateLimitExceed">BwRateLimitExceed</a>" : <i>Double</i>,
    "<a href="#bwratelimitresume" title="BwRateLimitResume">BwRateLimitResume</a>" : <i>Double</i>,
    "<a href="#gatewaydown" title="GatewayDown">GatewayDown</a>" : <i>Double</i>,
    "<a href="#gatewayup" title="GatewayUp">GatewayUp</a>" : <i>Double</i>,
    "<a href="#serverconnlimit" title="ServerConnLimit">ServerConnLimit</a>" : <i>Double</i>,
    "<a href="#serverconnresume" title="ServerConnResume">ServerConnResume</a>" : <i>Double</i>,
    "<a href="#serverdisabled" title="ServerDisabled">ServerDisabled</a>" : <i>Double</i>,
    "<a href="#serverdown" title="ServerDown">ServerDown</a>" : <i>Double</i>,
    "<a href="#serverselectionfailure" title="ServerSelectionFailure">ServerSelectionFailure</a>" : <i>Double</i>,
    "<a href="#serverup" title="ServerUp">ServerUp</a>" : <i>Double</i>,
    "<a href="#serviceconnlimit" title="ServiceConnLimit">ServiceConnLimit</a>" : <i>Double</i>,
    "<a href="#serviceconnresume" title="ServiceConnResume">ServiceConnResume</a>" : <i>Double</i>,
    "<a href="#servicedown" title="ServiceDown">ServiceDown</a>" : <i>Double</i>,
    "<a href="#servicegroupdown" title="ServiceGroupDown">ServiceGroupDown</a>" : <i>Double</i>,
    "<a href="#servicegroupmemberdown" title="ServiceGroupMemberDown">ServiceGroupMemberDown</a>" : <i>Double</i>,
    "<a href="#servicegroupmemberup" title="ServiceGroupMemberUp">ServiceGroupMemberUp</a>" : <i>Double</i>,
    "<a href="#servicegroupup" title="ServiceGroupUp">ServiceGroupUp</a>" : <i>Double</i>,
    "<a href="#serviceup" title="ServiceUp">ServiceUp</a>" : <i>Double</i>,
    "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
    "<a href="#vipconnlimit" title="VipConnlimit">VipConnlimit</a>" : <i>Double</i>,
    "<a href="#vipconnratelimit" title="VipConnratelimit">VipConnratelimit</a>" : <i>Double</i>,
    "<a href="#vipdown" title="VipDown">VipDown</a>" : <i>Double</i>,
    "<a href="#vipportconnlimit" title="VipPortConnlimit">VipPortConnlimit</a>" : <i>Double</i>,
    "<a href="#vipportconnratelimit" title="VipPortConnratelimit">VipPortConnratelimit</a>" : <i>Double</i>,
    "<a href="#vipportdown" title="VipPortDown">VipPortDown</a>" : <i>Double</i>,
    "<a href="#vipportup" title="VipPortUp">VipPortUp</a>" : <i>Double</i>,
    "<a href="#vipup" title="VipUp">VipUp</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#all" title="All">All</a>: <i>Double</i>
<a href="#applicationbufferlimit" title="ApplicationBufferLimit">ApplicationBufferLimit</a>: <i>Double</i>
<a href="#bwratelimitexceed" title="BwRateLimitExceed">BwRateLimitExceed</a>: <i>Double</i>
<a href="#bwratelimitresume" title="BwRateLimitResume">BwRateLimitResume</a>: <i>Double</i>
<a href="#gatewaydown" title="GatewayDown">GatewayDown</a>: <i>Double</i>
<a href="#gatewayup" title="GatewayUp">GatewayUp</a>: <i>Double</i>
<a href="#serverconnlimit" title="ServerConnLimit">ServerConnLimit</a>: <i>Double</i>
<a href="#serverconnresume" title="ServerConnResume">ServerConnResume</a>: <i>Double</i>
<a href="#serverdisabled" title="ServerDisabled">ServerDisabled</a>: <i>Double</i>
<a href="#serverdown" title="ServerDown">ServerDown</a>: <i>Double</i>
<a href="#serverselectionfailure" title="ServerSelectionFailure">ServerSelectionFailure</a>: <i>Double</i>
<a href="#serverup" title="ServerUp">ServerUp</a>: <i>Double</i>
<a href="#serviceconnlimit" title="ServiceConnLimit">ServiceConnLimit</a>: <i>Double</i>
<a href="#serviceconnresume" title="ServiceConnResume">ServiceConnResume</a>: <i>Double</i>
<a href="#servicedown" title="ServiceDown">ServiceDown</a>: <i>Double</i>
<a href="#servicegroupdown" title="ServiceGroupDown">ServiceGroupDown</a>: <i>Double</i>
<a href="#servicegroupmemberdown" title="ServiceGroupMemberDown">ServiceGroupMemberDown</a>: <i>Double</i>
<a href="#servicegroupmemberup" title="ServiceGroupMemberUp">ServiceGroupMemberUp</a>: <i>Double</i>
<a href="#servicegroupup" title="ServiceGroupUp">ServiceGroupUp</a>: <i>Double</i>
<a href="#serviceup" title="ServiceUp">ServiceUp</a>: <i>Double</i>
<a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
<a href="#vipconnlimit" title="VipConnlimit">VipConnlimit</a>: <i>Double</i>
<a href="#vipconnratelimit" title="VipConnratelimit">VipConnratelimit</a>: <i>Double</i>
<a href="#vipdown" title="VipDown">VipDown</a>: <i>Double</i>
<a href="#vipportconnlimit" title="VipPortConnlimit">VipPortConnlimit</a>: <i>Double</i>
<a href="#vipportconnratelimit" title="VipPortConnratelimit">VipPortConnratelimit</a>: <i>Double</i>
<a href="#vipportdown" title="VipPortDown">VipPortDown</a>: <i>Double</i>
<a href="#vipportup" title="VipPortUp">VipPortUp</a>: <i>Double</i>
<a href="#vipup" title="VipUp">VipUp</a>: <i>Double</i>
</pre>

## Properties

#### All

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationBufferLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BwRateLimitExceed

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BwRateLimitResume

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayDown

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayUp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerConnLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerConnResume

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerDisabled

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerDown

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSelectionFailure

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerUp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConnLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConnResume

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDown

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroupDown

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroupMemberDown

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroupMemberUp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroupUp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceUp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipConnlimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipConnratelimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipDown

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipPortConnlimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipPortConnratelimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipPortDown

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipPortUp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipUp

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

