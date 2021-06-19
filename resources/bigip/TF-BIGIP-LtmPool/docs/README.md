# TF::BIGIP::LtmPool

`bigip_ltm_pool` Manages F5 BIG-IP LTM pools via iControl REST API.

Resources should be named with their "full path". The full path is the combination of the partition + name (example: /Common/my-pool ) or  partition + directory + name of the resource  (example: /Common/test/my-pool )

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::LtmPool",
    "Properties" : {
        "<a href="#allownat" title="AllowNat">AllowNat</a>" : <i>String</i>,
        "<a href="#allowsnat" title="AllowSnat">AllowSnat</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#loadbalancingmode" title="LoadBalancingMode">LoadBalancingMode</a>" : <i>String</i>,
        "<a href="#minimumactivemembers" title="MinimumActiveMembers">MinimumActiveMembers</a>" : <i>Double</i>,
        "<a href="#monitors" title="Monitors">Monitors</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#reselecttries" title="ReselectTries">ReselectTries</a>" : <i>Double</i>,
        "<a href="#servicedownaction" title="ServiceDownAction">ServiceDownAction</a>" : <i>String</i>,
        "<a href="#slowramptime" title="SlowRampTime">SlowRampTime</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::LtmPool
Properties:
    <a href="#allownat" title="AllowNat">AllowNat</a>: <i>String</i>
    <a href="#allowsnat" title="AllowSnat">AllowSnat</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#loadbalancingmode" title="LoadBalancingMode">LoadBalancingMode</a>: <i>String</i>
    <a href="#minimumactivemembers" title="MinimumActiveMembers">MinimumActiveMembers</a>: <i>Double</i>
    <a href="#monitors" title="Monitors">Monitors</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#reselecttries" title="ReselectTries">ReselectTries</a>: <i>Double</i>
    <a href="#servicedownaction" title="ServiceDownAction">ServiceDownAction</a>: <i>String</i>
    <a href="#slowramptime" title="SlowRampTime">SlowRampTime</a>: <i>Double</i>
</pre>

## Properties

#### AllowNat

Specifies whether NATs are automatically enabled or disabled for any connections using this pool, [ Default : `yes`, Possible Values `yes` or `no`].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowSnat

Specifies whether SNATs are automatically enabled or disabled for any connections using this pool,[ Default : `yes`, Possible Values `yes` or `no`].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Specifies descriptive text that identifies the pool.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancingMode

Specifies the load balancing method. The default is Round Robin.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumActiveMembers

Specifies whether the system load balances traffic according to the priority number assigned to the pool member,Default Value is `0` meaning `disabled`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Monitors

List of monitor names to associate with the pool.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the pool,it should be "full path".The full path is the combination of the partition + name of the pool.(For example `/Common/my-pool`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReselectTries

Specifies the number of times the system tries to contact a new pool member after a passive failure.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceDownAction

Specifies how the system should respond when the target pool member becomes unavailable. The default is `None`, Possible values: `[none, reset, reselect, drop]`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlowRampTime

Specifies the duration during which the system sends less traffic to a newly-enabled pool member.

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

