# Terraform::Kubernetes::Deployment Spec InitContainer SecurityContext

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowprivilegeescalation" title="AllowPrivilegeEscalation">AllowPrivilegeEscalation</a>" : <i>Boolean</i>,
    "<a href="#privileged" title="Privileged">Privileged</a>" : <i>Boolean</i>,
    "<a href="#readonlyrootfilesystem" title="ReadOnlyRootFilesystem">ReadOnlyRootFilesystem</a>" : <i>Boolean</i>,
    "<a href="#runasgroup" title="RunAsGroup">RunAsGroup</a>" : <i>Double</i>,
    "<a href="#runasnonroot" title="RunAsNonRoot">RunAsNonRoot</a>" : <i>Boolean</i>,
    "<a href="#runasuser" title="RunAsUser">RunAsUser</a>" : <i>Double</i>,
    "<a href="#capabilities" title="Capabilities">Capabilities</a>" : <i>[ <a href="spec-initcontainer-securitycontext-capabilities.md">Capabilities</a>, ... ]</i>,
    "<a href="#selinuxoptions" title="SeLinuxOptions">SeLinuxOptions</a>" : <i>[ <a href="spec-initcontainer-securitycontext-selinuxoptions.md">SeLinuxOptions</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowprivilegeescalation" title="AllowPrivilegeEscalation">AllowPrivilegeEscalation</a>: <i>Boolean</i>
<a href="#privileged" title="Privileged">Privileged</a>: <i>Boolean</i>
<a href="#readonlyrootfilesystem" title="ReadOnlyRootFilesystem">ReadOnlyRootFilesystem</a>: <i>Boolean</i>
<a href="#runasgroup" title="RunAsGroup">RunAsGroup</a>: <i>Double</i>
<a href="#runasnonroot" title="RunAsNonRoot">RunAsNonRoot</a>: <i>Boolean</i>
<a href="#runasuser" title="RunAsUser">RunAsUser</a>: <i>Double</i>
<a href="#capabilities" title="Capabilities">Capabilities</a>: <i>
      - <a href="spec-initcontainer-securitycontext-capabilities.md">Capabilities</a></i>
<a href="#selinuxoptions" title="SeLinuxOptions">SeLinuxOptions</a>: <i>
      - <a href="spec-initcontainer-securitycontext-selinuxoptions.md">SeLinuxOptions</a></i>
</pre>

## Properties

#### AllowPrivilegeEscalation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privileged

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadOnlyRootFilesystem

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunAsGroup

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunAsNonRoot

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RunAsUser

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capabilities

_Required_: No

_Type_: List of <a href="spec-initcontainer-securitycontext-capabilities.md">Capabilities</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeLinuxOptions

_Required_: No

_Type_: List of <a href="spec-initcontainer-securitycontext-selinuxoptions.md">SeLinuxOptions</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

