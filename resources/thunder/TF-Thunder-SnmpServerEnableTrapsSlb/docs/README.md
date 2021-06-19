# TF::Thunder::SnmpServerEnableTrapsSlb

`thunder_snmp_server_enable_traps_slb` Provides details about thunder snmp server enable traps slb

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SnmpServerEnableTrapsSlb",
    "Properties" : {
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
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SnmpServerEnableTrapsSlb
Properties:
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

Enable all SLB traps.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationBufferLimit

Enable application buffer reach limit trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BwRateLimitExceed

Enable SLB server/port bandwidth rate limit exceed trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BwRateLimitResume

Enable SLB server/port bandwidth rate limit resume trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayDown

Enable SLB server gateway down trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GatewayUp

Enable SLB server gateway up trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerConnLimit

Enable SLB server connection limit trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerConnResume

Enable SLB server connection resume trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerDisabled

Enable SLB server-disabled trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerDown

Enable SLB server-down trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerSelectionFailure

Enable SLB server selection failure trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerUp

Enable slb server up trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConnLimit

Enable SLB service connection limit trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceConnResume

Enable SLB service connection resume trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDown

Enable SLB service-down trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroupDown

Enable SLB service-group-down trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroupMemberDown

Enable SLB service-group-member-down trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroupMemberUp

Enable SLB service-group-member-up trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceGroupUp

Enable SLB service-group-up trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceUp

Enable SLB service-up trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipConnlimit

Enable the virtual server reach conn-limit trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipConnratelimit

Enable the virtual server reach conn-rate-limit trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipDown

Enable SLB virtual server down trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipPortConnlimit

Enable the virtual port reach conn-limit trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipPortConnratelimit

Enable the virtual port reach conn-rate-limit trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipPortDown

Enable SLB virtual port down trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipPortUp

Enable SLB virtual port up trap.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipUp

Enable SLB virtual server up trap.

_Required_: No

_Type_: Double

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

