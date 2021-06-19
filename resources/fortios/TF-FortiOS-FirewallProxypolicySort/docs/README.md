# TF::FortiOS::FirewallProxypolicySort

Provides a resource to sort firewall proxypolicy policy

```hcl

resource "fortios_firewall_proxypolicy_sort" "test" {
  sortby        = "policyid"
  sortdirection = "ascending"
}
		
```

The following arguments are supported:

* `sortby` - (Required) Sort security policies by the value, it currently supports "policyid".
* `sortdirection` - (Required) Sort dirction, supports "ascending" and "descending".
* `force_recreate` - The argument is optional, if it is set, when the value changes, the resource will be re-created. It is usually used when new policies are added, or old policies are deleted.
* `comment` - Comment.
* `vdomparam` - Specifies the vdom to which the data source will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

The following attributes are exported:

* `id` - an identifier for the resource.
* `sortby` - Sort security policies by the value, it curre...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallProxypolicySort",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#forcerecreate" title="ForceRecreate">ForceRecreate</a>" : <i>String</i>,
        "<a href="#sortby" title="Sortby">Sortby</a>" : <i>String</i>,
        "<a href="#sortdirection" title="Sortdirection">Sortdirection</a>" : <i>String</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallProxypolicySort
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#forcerecreate" title="ForceRecreate">ForceRecreate</a>: <i>String</i>
    <a href="#sortby" title="Sortby">Sortby</a>: <i>String</i>
    <a href="#sortdirection" title="Sortdirection">Sortdirection</a>: <i>String</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
</pre>

## Properties

#### Comment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceRecreate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sortby

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sortdirection

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

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

