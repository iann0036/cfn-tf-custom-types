# TF::AzureRM::HpcCacheNfsTarget NamespaceJunctionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesspolicyname" title="AccessPolicyName">AccessPolicyName</a>" : <i>String</i>,
    "<a href="#namespacepath" title="NamespacePath">NamespacePath</a>" : <i>String</i>,
    "<a href="#nfsexport" title="NfsExport">NfsExport</a>" : <i>String</i>,
    "<a href="#targetpath" title="TargetPath">TargetPath</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accesspolicyname" title="AccessPolicyName">AccessPolicyName</a>: <i>String</i>
<a href="#namespacepath" title="NamespacePath">NamespacePath</a>: <i>String</i>
<a href="#nfsexport" title="NfsExport">NfsExport</a>: <i>String</i>
<a href="#targetpath" title="TargetPath">TargetPath</a>: <i>String</i>
</pre>

## Properties

#### AccessPolicyName

The name of the access policy applied to this target. Defaults to `default`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespacePath

The client-facing file path of this NFS target within the HPC Cache NFS Target.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NfsExport

The NFS export of this NFS target within the HPC Cache NFS Target.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TargetPath

The relative subdirectory path from the `nfs_export` to map to the `namespace_path`. Defaults to `""`, in which case the whole `nfs_export` is exported.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

