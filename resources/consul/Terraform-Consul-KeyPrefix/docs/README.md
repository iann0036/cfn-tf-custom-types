# Terraform::Consul::KeyPrefix

Allows Terraform to manage a "namespace" of Consul keys that share a common
name prefix.

Like `consul_keys`, this resource can write values into the Consul key/value
store, but *unlike* `consul_keys` this resource can detect and remove extra
keys that have been added some other way, thus ensuring that rogue data
added outside of Terraform will be removed on the next run.

This resource is thus useful in the case where Terraform is exclusively
managing a set of related keys.

To avoid accidentally clobbering matching data that existed in Consul before
a `consul_key_prefix` resource was created, creation of a key prefix instance
will fail if any matching keys are already present in the key/value store.
If any conflicting data is present, you must first delete it manually or
explicitly import the prefix.

~> **Warning** After this resource is instantiated, Terraform takes control
over *all* keys with the given path prefix, and will remove any matching keys
that are not present in the configuration. It will also delete *all* keys under
the given prefix when a `consul_key_prefix` resource is destroyed, even if
those keys were created outside of Terraform.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Consul::KeyPrefix",
    "Properties" : {
        "<a href="#datacenter" title="Datacenter">Datacenter</a>" : <i>String</i>,
        "<a href="#pathprefix" title="PathPrefix">PathPrefix</a>" : <i>String</i>,
        "<a href="#subkeys" title="Subkeys">Subkeys</a>" : <i>[ <a href="subkeys.md">Subkeys</a>, ... ]</i>,
        "<a href="#token" title="Token">Token</a>" : <i>String</i>,
        "<a href="#subkey" title="Subkey">Subkey</a>" : <i>[ <a href="subkey.md">Subkey</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Consul::KeyPrefix
Properties:
    <a href="#datacenter" title="Datacenter">Datacenter</a>: <i>String</i>
    <a href="#pathprefix" title="PathPrefix">PathPrefix</a>: <i>String</i>
    <a href="#subkeys" title="Subkeys">Subkeys</a>: <i>
      - <a href="subkeys.md">Subkeys</a></i>
    <a href="#token" title="Token">Token</a>: <i>String</i>
    <a href="#subkey" title="Subkey">Subkey</a>: <i>
      - <a href="subkey.md">Subkey</a></i>
</pre>

## Properties

#### Datacenter

The datacenter to use. This overrides the
agent's default datacenter and the datacenter in the provider setup.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PathPrefix

Specifies the common prefix shared by all keys
that will be managed by this resource instance. In most cases this will
end with a slash, to manage a "folder" of keys.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subkeys

A mapping from subkey name (which will be appended
to the given `path_prefix`) to the value that should be stored at that key.
Use slashes, as shown in the above example, to create "sub-folders" under
the given path prefix.

_Required_: No

_Type_: List of <a href="subkeys.md">Subkeys</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

The ACL token to use. This overrides the
token that the agent provides by default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subkey

_Required_: No

_Type_: List of <a href="subkey.md">Subkey</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

