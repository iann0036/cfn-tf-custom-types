# TF::FortiOS::FirewallSecurityPolicyseq

Provides a resource to alter firewall security policy sequence

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallSecurityPolicyseq",
    "Properties" : {
        "<a href="#alterposition" title="AlterPosition">AlterPosition</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#enablestatechecking" title="EnableStateChecking">EnableStateChecking</a>" : <i>Boolean</i>,
        "<a href="#policydstid" title="PolicyDstId">PolicyDstId</a>" : <i>Double</i>,
        "<a href="#policysrcid" title="PolicySrcId">PolicySrcId</a>" : <i>Double</i>,
        "<a href="#statepolicysrcdstpos" title="StatePolicySrcdstPos">StatePolicySrcdstPos</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallSecurityPolicyseq
Properties:
    <a href="#alterposition" title="AlterPosition">AlterPosition</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#enablestatechecking" title="EnableStateChecking">EnableStateChecking</a>: <i>Boolean</i>
    <a href="#policydstid" title="PolicyDstId">PolicyDstId</a>: <i>Double</i>
    <a href="#policysrcid" title="PolicySrcId">PolicySrcId</a>: <i>Double</i>
    <a href="#statepolicysrcdstpos" title="StatePolicySrcdstPos">StatePolicySrcdstPos</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### AlterPosition

The alter position: should only be "before" or "after".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableStateChecking

Enable status detection for policy_src_id and policy_dst_id, to detect whether they have been changed outside of terraform, the default is false. If this parameter is true, when policy_src_id and policy_dst_id are modified or deleted outside the terraform, the resource will be able to detect the change, in other words, terraform plan can detect the change. When this parameter is false, if policy_src_id and policy_dst_id are modified or deleted outside the terraform, the change will not be detected by the resource, which means that the terraform plan will think that the state has not changed. The main purpose of this argument is to make the resource compatible with the old version. If you use this resource for the first time now, it is recommended to set it to true. For detailed usage, see "Attributes Reference" and "A More Detailed Example" below.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyDstId

The dest policy id which you want to alter.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicySrcId

The policy id which you want to alter.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StatePolicySrcdstPos

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

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

#### StatePolicyList

Returns the <code>StatePolicyList</code> value.

