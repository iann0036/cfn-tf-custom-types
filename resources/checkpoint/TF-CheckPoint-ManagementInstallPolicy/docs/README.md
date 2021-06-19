# TF::CheckPoint::ManagementInstallPolicy

This command resource allows you to install the published policy.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementInstallPolicy",
    "Properties" : {
        "<a href="#access" title="Access">Access</a>" : <i>Boolean</i>,
        "<a href="#desktopsecurity" title="DesktopSecurity">DesktopSecurity</a>" : <i>Boolean</i>,
        "<a href="#installonallclustermembersorfail" title="InstallOnAllClusterMembersOrFail">InstallOnAllClusterMembersOrFail</a>" : <i>Boolean</i>,
        "<a href="#policypackage" title="PolicyPackage">PolicyPackage</a>" : <i>String</i>,
        "<a href="#prepareonly" title="PrepareOnly">PrepareOnly</a>" : <i>Boolean</i>,
        "<a href="#qos" title="Qos">Qos</a>" : <i>Boolean</i>,
        "<a href="#revision" title="Revision">Revision</a>" : <i>String</i>,
        "<a href="#targets" title="Targets">Targets</a>" : <i>[ String, ... ]</i>,
        "<a href="#threatprevention" title="ThreatPrevention">ThreatPrevention</a>" : <i>Boolean</i>,
        "<a href="#triggers" title="Triggers">Triggers</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementInstallPolicy
Properties:
    <a href="#access" title="Access">Access</a>: <i>Boolean</i>
    <a href="#desktopsecurity" title="DesktopSecurity">DesktopSecurity</a>: <i>Boolean</i>
    <a href="#installonallclustermembersorfail" title="InstallOnAllClusterMembersOrFail">InstallOnAllClusterMembersOrFail</a>: <i>Boolean</i>
    <a href="#policypackage" title="PolicyPackage">PolicyPackage</a>: <i>String</i>
    <a href="#prepareonly" title="PrepareOnly">PrepareOnly</a>: <i>Boolean</i>
    <a href="#qos" title="Qos">Qos</a>: <i>Boolean</i>
    <a href="#revision" title="Revision">Revision</a>: <i>String</i>
    <a href="#targets" title="Targets">Targets</a>: <i>
      - String</i>
    <a href="#threatprevention" title="ThreatPrevention">ThreatPrevention</a>: <i>Boolean</i>
    <a href="#triggers" title="Triggers">Triggers</a>: <i>
      - String</i>
</pre>

## Properties

#### Access

Set to be true in order to install the Access Control policy. By default, the value is true if Access Control policy is enabled on the input policy package, otherwise false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DesktopSecurity

Set to be true in order to install the Desktop Security policy. By default, the value is true if desktop security policy is enabled on the input policy package, otherwise false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstallOnAllClusterMembersOrFail

Relevant for the gateway clusters. If true, the policy is installed on all the cluster members. If the installation on a cluster member fails, don't install on that cluster.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyPackage

The name of the Policy Package to be installed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrepareOnly

If true, prepares the policy for the installation, but doesn't install it on an installation target.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Qos

Set to be true in order to install the QoS policy. By default, the value is true if Quality-of-Service policy is enabled on the input policy package, otherwise false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Revision

The UID of the revision of the policy to install.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Targets

On what targets to execute this command. Targets may be identified by their name, or object unique identifier.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThreatPrevention

Set to be true in order to install the Threat Prevention policy. By default, the value is true if Threat Prevention policy is enabled on the input policy package, otherwise false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Triggers

Triggers a install-policy if there are any changes to objects in this list.

_Required_: No

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

