# Terraform::Cobbler::Repo

Manages a repo within Cobbler.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Cobbler::Repo",
    "Properties" : {
        "<a href="#aptcomponents" title="AptComponents">AptComponents</a>" : <i>[ String, ... ]</i>,
        "<a href="#aptdists" title="AptDists">AptDists</a>" : <i>[ String, ... ]</i>,
        "<a href="#arch" title="Arch">Arch</a>" : <i>String</i>,
        "<a href="#breed" title="Breed">Breed</a>" : <i>String</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#createrepoflags" title="CreaterepoFlags">CreaterepoFlags</a>" : <i>String</i>,
        "<a href="#environment" title="Environment">Environment</a>" : <i>String</i>,
        "<a href="#keepupdated" title="KeepUpdated">KeepUpdated</a>" : <i>Boolean</i>,
        "<a href="#mirror" title="Mirror">Mirror</a>" : <i>String</i>,
        "<a href="#mirrorlocally" title="MirrorLocally">MirrorLocally</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#proxy" title="Proxy">Proxy</a>" : <i>String</i>,
        "<a href="#rpmlist" title="RpmList">RpmList</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Cobbler::Repo
Properties:
    <a href="#aptcomponents" title="AptComponents">AptComponents</a>: <i>
      - String</i>
    <a href="#aptdists" title="AptDists">AptDists</a>: <i>
      - String</i>
    <a href="#arch" title="Arch">Arch</a>: <i>String</i>
    <a href="#breed" title="Breed">Breed</a>: <i>String</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#createrepoflags" title="CreaterepoFlags">CreaterepoFlags</a>: <i>String</i>
    <a href="#environment" title="Environment">Environment</a>: <i>String</i>
    <a href="#keepupdated" title="KeepUpdated">KeepUpdated</a>: <i>Boolean</i>
    <a href="#mirror" title="Mirror">Mirror</a>: <i>String</i>
    <a href="#mirrorlocally" title="MirrorLocally">MirrorLocally</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#proxy" title="Proxy">Proxy</a>: <i>String</i>
    <a href="#rpmlist" title="RpmList">RpmList</a>: <i>
      - String</i>
</pre>

## Properties

#### AptComponents

List of Apt components such as main,
restricted, universe. Applicable to apt breeds only.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AptDists

List of Apt distribution names such as trusty,
trusty-updates. Applicable to apt breeds only.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arch

The architecture of the repo. Valid options
are: i386, x86_64, ia64, ppc, ppc64, s390, arm.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Breed

The "breed" of distribution. Valid options
are: rsync, rhn, yum, apt, and wget. These choices may vary depending on the
version of Cobbler in use.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Free form text description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreaterepoFlags

Flags to use with `createrepo`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

Environment variables to use during repo command
execution.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeepUpdated

Update the repo upon Cobbler sync. Valid values
are true or false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mirror

Address of the repo to mirror.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MirrorLocally

Whether to copy the files locally or just
references to the external files. Valid values are true or false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A name for the repo.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owners

List of Owners for authz_ownership.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Proxy

Proxy to use for downloading the repo. This argument does
not work on older versions of Cobbler.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RpmList

List of specific RPMs to mirror.

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

