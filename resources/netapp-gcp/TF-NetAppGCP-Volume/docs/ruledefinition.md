# TF::NetAppGCP::Volume RuleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#access" title="Access">Access</a>" : <i>String</i>,
    "<a href="#allowedclients" title="AllowedClients">AllowedClients</a>" : <i>String</i>,
    "<a href="#hasrootaccess" title="HasRootAccess">HasRootAccess</a>" : <i>String</i>,
    "<a href="#kerberos5readonly" title="Kerberos5Readonly">Kerberos5Readonly</a>" : <i>Boolean</i>,
    "<a href="#kerberos5readwrite" title="Kerberos5Readwrite">Kerberos5Readwrite</a>" : <i>Boolean</i>,
    "<a href="#kerberos5ireadonly" title="Kerberos5iReadonly">Kerberos5iReadonly</a>" : <i>Boolean</i>,
    "<a href="#kerberos5ireadwrite" title="Kerberos5iReadwrite">Kerberos5iReadwrite</a>" : <i>Boolean</i>,
    "<a href="#kerberos5preadonly" title="Kerberos5pReadonly">Kerberos5pReadonly</a>" : <i>Boolean</i>,
    "<a href="#kerberos5preadwrite" title="Kerberos5pReadwrite">Kerberos5pReadwrite</a>" : <i>Boolean</i>,
    "<a href="#nfsv3" title="Nfsv3">Nfsv3</a>" : <i>[ <a href="nfsv3definition.md">Nfsv3Definition</a>, ... ]</i>,
    "<a href="#nfsv4" title="Nfsv4">Nfsv4</a>" : <i>[ <a href="nfsv4definition.md">Nfsv4Definition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#access" title="Access">Access</a>: <i>String</i>
<a href="#allowedclients" title="AllowedClients">AllowedClients</a>: <i>String</i>
<a href="#hasrootaccess" title="HasRootAccess">HasRootAccess</a>: <i>String</i>
<a href="#kerberos5readonly" title="Kerberos5Readonly">Kerberos5Readonly</a>: <i>Boolean</i>
<a href="#kerberos5readwrite" title="Kerberos5Readwrite">Kerberos5Readwrite</a>: <i>Boolean</i>
<a href="#kerberos5ireadonly" title="Kerberos5iReadonly">Kerberos5iReadonly</a>: <i>Boolean</i>
<a href="#kerberos5ireadwrite" title="Kerberos5iReadwrite">Kerberos5iReadwrite</a>: <i>Boolean</i>
<a href="#kerberos5preadonly" title="Kerberos5pReadonly">Kerberos5pReadonly</a>: <i>Boolean</i>
<a href="#kerberos5preadwrite" title="Kerberos5pReadwrite">Kerberos5pReadwrite</a>: <i>Boolean</i>
<a href="#nfsv3" title="Nfsv3">Nfsv3</a>: <i>
      - <a href="nfsv3definition.md">Nfsv3Definition</a></i>
<a href="#nfsv4" title="Nfsv4">Nfsv4</a>: <i>
      - <a href="nfsv4definition.md">Nfsv4Definition</a></i>
</pre>

## Properties

#### Access

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedClients

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HasRootAccess

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kerberos5Readonly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kerberos5Readwrite

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kerberos5iReadonly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kerberos5iReadwrite

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kerberos5pReadonly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Kerberos5pReadwrite

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nfsv3

_Required_: No

_Type_: List of <a href="nfsv3definition.md">Nfsv3Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Nfsv4

_Required_: No

_Type_: List of <a href="nfsv4definition.md">Nfsv4Definition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

