# TF::Turbot::Mod

The `Turbot Mod` resource adds support to install, update and uninstall a mod. The currently installed mod will be validated against the desired version, and the appropriate action will be taken. Removing a mod from the config will uninstall the mod.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Turbot::Mod",
    "Properties" : {
        "<a href="#mod" title="Mod">Mod</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Turbot::Mod
Properties:
    <a href="#mod" title="Mod">Mod</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Mod

The mod to be installed, updated or uninstalled. For example, `aws-s3`.
- `org` - (Required) The parent author of the mod.
- `parent` - (Optional) Installation point for the mod in the resource hierarchy. Defaults to the Turbot root resource.
- `version` - (Optional) The version to be installed, e.g. `5.1.3`. If a semantic version range is given, e.g. `^5` then the latest available version from that range will be installed. Defaults to `*`, which is the latest available version of the mod.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The parent author of the mod.
- `parent` - (Optional) Installation point for the mod in the resource hierarchy. Defaults to the Turbot root resource.
- `version` - (Optional) The version to be installed, e.g. `5.1.3`. If a semantic version range is given, e.g. `^5` then the latest available version from that range will be installed. Defaults to `*`, which is the latest available version of the mod.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

Installation point for the mod in the resource hierarchy. Defaults to the Turbot root resource.
- `version` - (Optional) The version to be installed, e.g. `5.1.3`. If a semantic version range is given, e.g. `^5` then the latest available version from that range will be installed. Defaults to `*`, which is the latest available version of the mod.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

The version to be installed, e.g. `5.1.3`. If a semantic version range is given, e.g. `^5` then the latest available version from that range will be installed. Defaults to `*`, which is the latest available version of the mod.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### ParentAkas

Returns the <code>ParentAkas</code> value.

#### Uri

Returns the <code>Uri</code> value.

#### VersionCurrent

Returns the <code>VersionCurrent</code> value.

#### VersionLatest

Returns the <code>VersionLatest</code> value.

