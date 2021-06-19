# TF::Limelight::Delivery

This resource provides a way to configure Content Delivery in Limelight Networks.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Limelight::Delivery",
    "Properties" : {
        "<a href="#publishedhostname" title="PublishedHostname">PublishedHostname</a>" : <i>String</i>,
        "<a href="#publishedpath" title="PublishedPath">PublishedPath</a>" : <i>String</i>,
        "<a href="#serviceprofile" title="ServiceProfile">ServiceProfile</a>" : <i>String</i>,
        "<a href="#shortname" title="Shortname">Shortname</a>" : <i>String</i>,
        "<a href="#sourcehostname" title="SourceHostname">SourceHostname</a>" : <i>String</i>,
        "<a href="#sourcepath" title="SourcePath">SourcePath</a>" : <i>String</i>,
        "<a href="#protocolset" title="ProtocolSet">ProtocolSet</a>" : <i>[ <a href="protocolsetdefinition.md">ProtocolSetDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Limelight::Delivery
Properties:
    <a href="#publishedhostname" title="PublishedHostname">PublishedHostname</a>: <i>String</i>
    <a href="#publishedpath" title="PublishedPath">PublishedPath</a>: <i>String</i>
    <a href="#serviceprofile" title="ServiceProfile">ServiceProfile</a>: <i>String</i>
    <a href="#shortname" title="Shortname">Shortname</a>: <i>String</i>
    <a href="#sourcehostname" title="SourceHostname">SourceHostname</a>: <i>String</i>
    <a href="#sourcepath" title="SourcePath">SourcePath</a>: <i>String</i>
    <a href="#protocolset" title="ProtocolSet">ProtocolSet</a>: <i>
      - <a href="protocolsetdefinition.md">ProtocolSetDefinition</a></i>
</pre>

## Properties

#### PublishedHostname

Published hostname for the content.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishedPath

Published path for the content.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceProfile

Service profile to use. Defaults to `LLNW-Generic`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shortname

The account name (shortname).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceHostname

Source (origin) hostname for the content.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourcePath

Source path on the origin for the content.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProtocolSet

_Required_: No

_Type_: List of <a href="protocolsetdefinition.md">ProtocolSetDefinition</a>

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

#### VersionNumber

Returns the <code>VersionNumber</code> value.

