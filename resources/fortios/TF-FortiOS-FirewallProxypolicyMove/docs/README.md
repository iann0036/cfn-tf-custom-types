# TF::FortiOS::FirewallProxypolicyMove

Provides a resource to move firewall proxypolicy policy

```hcl

resource "fortios_firewall_proxypolicy_move" "test1" {
  policyid_src = 2
  policyid_dst = 3
  move         = "after"
}
		
```

The following arguments are supported:

* `policyid_src` - (Required) The item's id which you want to move
* `policyid_dst` - (Required) The target item's id of the move action
* `move` - (Required) The move action. Valid values: `before`, `after`
* `comment` - Comment
* `vdomparam` - Specifies the vdom to which the data source will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

The following attributes are exported:

* `id` - an identifier for the resource.
* `policyid_src` - The item's id which you want to move
* `policyid_dst` - The target item's id of the move action
* `move` - (Required) the move action. Valid values: `before`, `after`
* `comment` - Comment
* `state_poli...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallProxypolicyMove",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#move" title="Move">Move</a>" : <i>String</i>,
        "<a href="#policyiddst" title="PolicyidDst">PolicyidDst</a>" : <i>Double</i>,
        "<a href="#policyidsrc" title="PolicyidSrc">PolicyidSrc</a>" : <i>Double</i>,
        "<a href="#statepolicysrcdstpos" title="StatePolicySrcdstPos">StatePolicySrcdstPos</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallProxypolicyMove
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#move" title="Move">Move</a>: <i>String</i>
    <a href="#policyiddst" title="PolicyidDst">PolicyidDst</a>: <i>Double</i>
    <a href="#policyidsrc" title="PolicyidSrc">PolicyidSrc</a>: <i>Double</i>
    <a href="#statepolicysrcdstpos" title="StatePolicySrcdstPos">StatePolicySrcdstPos</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Comment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Move

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyidDst

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyidSrc

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

