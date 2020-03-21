# Terraform::Rundeck::Project

The project resource allows Rundeck projects to be managed by Terraform. In Rundeck a project
is the container object for a set of jobs and the configuration for which servers those jobs
can be run on.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Rundeck::Project",
    "Properties" : {
        "<a href="#defaultnodeexecutorplugin" title="DefaultNodeExecutorPlugin">DefaultNodeExecutorPlugin</a>" : <i>String</i>,
        "<a href="#defaultnodefilecopierplugin" title="DefaultNodeFileCopierPlugin">DefaultNodeFileCopierPlugin</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#extraconfig" title="ExtraConfig">ExtraConfig</a>" : <i>[ <a href="extraconfig.md">ExtraConfig</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#sshauthenticationtype" title="SshAuthenticationType">SshAuthenticationType</a>" : <i>String</i>,
        "<a href="#sshkeyfilepath" title="SshKeyFilePath">SshKeyFilePath</a>" : <i>String</i>,
        "<a href="#sshkeystoragepath" title="SshKeyStoragePath">SshKeyStoragePath</a>" : <i>String</i>,
        "<a href="#resourcemodelsource" title="ResourceModelSource">ResourceModelSource</a>" : <i>[ <a href="resourcemodelsource.md">ResourceModelSource</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Rundeck::Project
Properties:
    <a href="#defaultnodeexecutorplugin" title="DefaultNodeExecutorPlugin">DefaultNodeExecutorPlugin</a>: <i>String</i>
    <a href="#defaultnodefilecopierplugin" title="DefaultNodeFileCopierPlugin">DefaultNodeFileCopierPlugin</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#extraconfig" title="ExtraConfig">ExtraConfig</a>: <i>
      - <a href="extraconfig.md">ExtraConfig</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#sshauthenticationtype" title="SshAuthenticationType">SshAuthenticationType</a>: <i>String</i>
    <a href="#sshkeyfilepath" title="SshKeyFilePath">SshKeyFilePath</a>: <i>String</i>
    <a href="#sshkeystoragepath" title="SshKeyStoragePath">SshKeyStoragePath</a>: <i>String</i>
    <a href="#resourcemodelsource" title="ResourceModelSource">ResourceModelSource</a>: <i>
      - <a href="resourcemodelsource.md">ResourceModelSource</a></i>
</pre>

## Properties

#### DefaultNodeExecutorPlugin

The name of a plugin to use to run commands on
nodes within this project. Defaults to `jsch-ssh`, which uses the SSH protocol to access the
nodes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultNodeFileCopierPlugin

The name of a plugin to use to copy files onto
nodes within this project. Defaults to `jsch-scp`, which uses the "Secure Copy" protocol
to send files over SSH.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A description of the project, to be displayed in the Rundeck UI.
Defaults to "Managed by Terraform".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraConfig

Behind the scenes a Rundeck project is really an arbitrary set of
key/value pairs. This map argument allows setting any configuration properties that aren't
explicitly supported by the other arguments described above, but due to limitations of Terraform
the key names must be written with slashes in place of dots. Do not use this argument to set
properties that the above arguments set, or undefined behavior will result.

_Required_: No

_Type_: List of <a href="extraconfig.md">ExtraConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the project, used both in the UI and to uniquely identify
the project. Must therefore be unique across a single Rundeck installation.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshAuthenticationType

When the SSH-based file copier and executor plugins are
used, the type of SSH authentication to use. Defaults to `privateKey`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeyFilePath

Like `ssh_key_storage_path` except that the key is read from
the Rundeck server's local filesystem, rather than from the key store.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SshKeyStoragePath

When the SSH-based file copier and executor plugins are
used, the location within Rundeck's key store where the SSH private key can be found. Private
keys can be uploaded to rundeck using the `rundeck_private_key` resource.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceModelSource

_Required_: No

_Type_: List of <a href="resourcemodelsource.md">ResourceModelSource</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### UiUrl

Returns the <code>UiUrl</code> value.

