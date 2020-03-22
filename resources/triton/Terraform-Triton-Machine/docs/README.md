# Terraform::Triton::Machine

The `triton_machine` resource represents a virtual machine or infrastructure container running in Triton.

~> **Note:** Starting with Triton 0.2.0, Please note that when you want to specify the networks that you want the machine to be attached to, use the `networks` parameter
and not the `nic` parameter.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Triton::Machine",
    "Properties" : {
        "<a href="#administratorpw" title="AdministratorPw">AdministratorPw</a>" : <i>String</i>,
        "<a href="#affinity" title="Affinity">Affinity</a>" : <i>[ String, ... ]</i>,
        "<a href="#cloudconfig" title="CloudConfig">CloudConfig</a>" : <i>String</i>,
        "<a href="#deletionprotectionenabled" title="DeletionProtectionEnabled">DeletionProtectionEnabled</a>" : <i>Boolean</i>,
        "<a href="#firewallenabled" title="FirewallEnabled">FirewallEnabled</a>" : <i>Boolean</i>,
        "<a href="#image" title="Image">Image</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networks" title="Networks">Networks</a>" : <i>[ String, ... ]</i>,
        "<a href="#package" title="Package">Package</a>" : <i>String</i>,
        "<a href="#rootauthorizedkeys" title="RootAuthorizedKeys">RootAuthorizedKeys</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#userdata" title="UserData">UserData</a>" : <i>String</i>,
        "<a href="#userscript" title="UserScript">UserScript</a>" : <i>String</i>,
        "<a href="#cns" title="Cns">Cns</a>" : <i>[ <a href="cns.md">Cns</a>, ... ]</i>,
        "<a href="#locality" title="Locality">Locality</a>" : <i>[ <a href="locality.md">Locality</a>, ... ]</i>,
        "<a href="#nic" title="Nic">Nic</a>" : <i>[ <a href="nic.md">Nic</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Triton::Machine
Properties:
    <a href="#administratorpw" title="AdministratorPw">AdministratorPw</a>: <i>String</i>
    <a href="#affinity" title="Affinity">Affinity</a>: <i>
      - String</i>
    <a href="#cloudconfig" title="CloudConfig">CloudConfig</a>: <i>String</i>
    <a href="#deletionprotectionenabled" title="DeletionProtectionEnabled">DeletionProtectionEnabled</a>: <i>Boolean</i>
    <a href="#firewallenabled" title="FirewallEnabled">FirewallEnabled</a>: <i>Boolean</i>
    <a href="#image" title="Image">Image</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networks" title="Networks">Networks</a>: <i>
      - String</i>
    <a href="#package" title="Package">Package</a>: <i>String</i>
    <a href="#rootauthorizedkeys" title="RootAuthorizedKeys">RootAuthorizedKeys</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#userdata" title="UserData">UserData</a>: <i>String</i>
    <a href="#userscript" title="UserScript">UserScript</a>: <i>String</i>
    <a href="#cns" title="Cns">Cns</a>: <i>
      - <a href="cns.md">Cns</a></i>
    <a href="#locality" title="Locality">Locality</a>: <i>
      - <a href="locality.md">Locality</a></i>
    <a href="#nic" title="Nic">Nic</a>: <i>
      - <a href="nic.md">Nic</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AdministratorPw

The initial password for the Administrator user. Only used for Windows virtual machines.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Affinity

A list of valid [Affinity Rules](https://apidocs.joyent.com/cloudapi/#affinity-rules) to apply to the machine which assist in data center placement. Using this attribute will force resource creation to be serial. NOTE: Affinity rules are best guess and assist in placing instances across a data center. They're used at creation and not referenced after.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudConfig

Cloud-init configuration for Linux brand machines, used instead of `user_data`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeletionProtectionEnabled

Whether an instance is destroyable. Default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallEnabled

Default: `false`
Whether the cloud firewall should be enabled for this machine.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

The UUID of the image to provision.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

A mapping of metadata to apply to the machine.

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The friendly name for the machine. Triton will generate a name if one is not specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Networks

The list of networks to associate with the machine. The network ID will be in hex form, e.g `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Package

The name of the package to use for provisioning.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RootAuthorizedKeys

The public keys authorized for root access via SSH to the machine.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to apply to the machine.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserData

Data to be copied to the machine on boot. **NOTE:** The content of `user_data`
will _not be executed_ on boot. The data will only be written to the file on each
boot before the content of the script from `user_script` is to be run.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserScript

The user script to run on boot (every boot on SmartMachines). To learn more about
both the user script and user data see the [metadata API][2] documentation and the
[Joyent Metadata Data Dictionary][1] specification.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cns

_Required_: No

_Type_: List of <a href="cns.md">Cns</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locality

_Required_: No

_Type_: List of <a href="locality.md">Locality</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nic

_Required_: No

_Type_: List of <a href="nic.md">Nic</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ComputeNode

Returns the <code>ComputeNode</code> value.

#### Created

Returns the <code>Created</code> value.

#### Dataset

Returns the <code>Dataset</code> value.

#### Disk

Returns the <code>Disk</code> value.

#### DomainNames

Returns the <code>DomainNames</code> value.

#### Id

Returns the <code>Id</code> value.

#### Ips

Returns the <code>Ips</code> value.

#### Memory

Returns the <code>Memory</code> value.

#### Primaryip

Returns the <code>Primaryip</code> value.

#### Type

Returns the <code>Type</code> value.

#### Updated

Returns the <code>Updated</code> value.

