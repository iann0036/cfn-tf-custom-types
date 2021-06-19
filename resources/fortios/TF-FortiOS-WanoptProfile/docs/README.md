# TF::FortiOS::WanoptProfile

Configure WAN optimization profiles.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::WanoptProfile",
    "Properties" : {
        "<a href="#authgroup" title="AuthGroup">AuthGroup</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#transparent" title="Transparent">Transparent</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#cifs" title="Cifs">Cifs</a>" : <i>[ <a href="cifsdefinition.md">CifsDefinition</a>, ... ]</i>,
        "<a href="#ftp" title="Ftp">Ftp</a>" : <i>[ <a href="ftpdefinition.md">FtpDefinition</a>, ... ]</i>,
        "<a href="#http" title="Http">Http</a>" : <i>[ <a href="httpdefinition.md">HttpDefinition</a>, ... ]</i>,
        "<a href="#mapi" title="Mapi">Mapi</a>" : <i>[ <a href="mapidefinition.md">MapiDefinition</a>, ... ]</i>,
        "<a href="#tcp" title="Tcp">Tcp</a>" : <i>[ <a href="tcpdefinition.md">TcpDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::WanoptProfile
Properties:
    <a href="#authgroup" title="AuthGroup">AuthGroup</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#transparent" title="Transparent">Transparent</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#cifs" title="Cifs">Cifs</a>: <i>
      - <a href="cifsdefinition.md">CifsDefinition</a></i>
    <a href="#ftp" title="Ftp">Ftp</a>: <i>
      - <a href="ftpdefinition.md">FtpDefinition</a></i>
    <a href="#http" title="Http">Http</a>: <i>
      - <a href="httpdefinition.md">HttpDefinition</a></i>
    <a href="#mapi" title="Mapi">Mapi</a>: <i>
      - <a href="mapidefinition.md">MapiDefinition</a></i>
    <a href="#tcp" title="Tcp">Tcp</a>: <i>
      - <a href="tcpdefinition.md">TcpDefinition</a></i>
</pre>

## Properties

#### AuthGroup

Optionally add an authentication group to restrict access to the WAN Optimization tunnel to peers in the authentication group.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Profile name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Transparent

Enable/disable transparent mode. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cifs

_Required_: No

_Type_: List of <a href="cifsdefinition.md">CifsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ftp

_Required_: No

_Type_: List of <a href="ftpdefinition.md">FtpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http

_Required_: No

_Type_: List of <a href="httpdefinition.md">HttpDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Mapi

_Required_: No

_Type_: List of <a href="mapidefinition.md">MapiDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tcp

_Required_: No

_Type_: List of <a href="tcpdefinition.md">TcpDefinition</a>

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

