# TF::AWS::DatasyncLocationNfs

Manages an NFS Location within AWS DataSync.

~> **NOTE:** The DataSync Agents must be available before creating this resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::DatasyncLocationNfs",
    "Properties" : {
        "<a href="#serverhostname" title="ServerHostname">ServerHostname</a>" : <i>String</i>,
        "<a href="#subdirectory" title="Subdirectory">Subdirectory</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#mountoptions" title="MountOptions">MountOptions</a>" : <i>[ <a href="mountoptionsdefinition.md">MountOptionsDefinition</a>, ... ]</i>,
        "<a href="#onpremconfig" title="OnPremConfig">OnPremConfig</a>" : <i>[ <a href="onpremconfigdefinition.md">OnPremConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::DatasyncLocationNfs
Properties:
    <a href="#serverhostname" title="ServerHostname">ServerHostname</a>: <i>String</i>
    <a href="#subdirectory" title="Subdirectory">Subdirectory</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#mountoptions" title="MountOptions">MountOptions</a>: <i>
      - <a href="mountoptionsdefinition.md">MountOptionsDefinition</a></i>
    <a href="#onpremconfig" title="OnPremConfig">OnPremConfig</a>: <i>
      - <a href="onpremconfigdefinition.md">OnPremConfigDefinition</a></i>
</pre>

## Properties

#### ServerHostname

Specifies the IP address or DNS name of the NFS server. The DataSync Agent(s) use this to mount the NFS server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subdirectory

Subdirectory to perform actions as source or destination. Should be exported by the NFS server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value pairs of resource tags to assign to the DataSync Location. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MountOptions

_Required_: No

_Type_: List of <a href="mountoptionsdefinition.md">MountOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnPremConfig

_Required_: No

_Type_: List of <a href="onpremconfigdefinition.md">OnPremConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.

#### Uri

Returns the <code>Uri</code> value.

