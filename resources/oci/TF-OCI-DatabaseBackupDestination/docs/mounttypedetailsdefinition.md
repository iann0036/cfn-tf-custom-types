# TF::OCI::DatabaseBackupDestination MountTypeDetailsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#localmountpointpath" title="LocalMountPointPath">LocalMountPointPath</a>" : <i>String</i>,
    "<a href="#mounttype" title="MountType">MountType</a>" : <i>String</i>,
    "<a href="#nfsserver" title="NfsServer">NfsServer</a>" : <i>[ String, ... ]</i>,
    "<a href="#nfsserverexport" title="NfsServerExport">NfsServerExport</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#localmountpointpath" title="LocalMountPointPath">LocalMountPointPath</a>: <i>String</i>
<a href="#mounttype" title="MountType">MountType</a>: <i>String</i>
<a href="#nfsserver" title="NfsServer">NfsServer</a>: <i>
      - String</i>
<a href="#nfsserverexport" title="NfsServerExport">NfsServerExport</a>: <i>String</i>
</pre>

## Properties

#### LocalMountPointPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NfsServer

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NfsServerExport

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

