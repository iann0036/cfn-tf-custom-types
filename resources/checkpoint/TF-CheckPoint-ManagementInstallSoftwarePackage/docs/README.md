# TF::CheckPoint::ManagementInstallSoftwarePackage

This command resource allows you to execute Check Point Install Software Package.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementInstallSoftwarePackage",
    "Properties" : {
        "<a href="#clusterinstallationsettings" title="ClusterInstallationSettings">ClusterInstallationSettings</a>" : <i>[ <a href="clusterinstallationsettingsdefinition.md">ClusterInstallationSettingsDefinition</a>, ... ]</i>,
        "<a href="#concurrencylimit" title="ConcurrencyLimit">ConcurrencyLimit</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#targets" title="Targets">Targets</a>" : <i>[ String, ... ]</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementInstallSoftwarePackage
Properties:
    <a href="#clusterinstallationsettings" title="ClusterInstallationSettings">ClusterInstallationSettings</a>: <i>
      - <a href="clusterinstallationsettingsdefinition.md">ClusterInstallationSettingsDefinition</a></i>
    <a href="#concurrencylimit" title="ConcurrencyLimit">ConcurrencyLimit</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#targets" title="Targets">Targets</a>: <i>
      - String</i>
</pre>

## Properties

#### ClusterInstallationSettings

Installation settings for cluster.cluster_installation_settings blocks are documented below.

_Required_: No

_Type_: List of <a href="clusterinstallationsettingsdefinition.md">ClusterInstallationSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConcurrencyLimit

The number of targets, on which the same package is installed at the same time.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the software package.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Targets

On what targets to execute this command. Targets may be identified by their name, or object unique identifier.targets blocks are documented below.

_Required_: Yes

_Type_: List of String

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

#### TaskId

Asynchronous task unique identifier.

