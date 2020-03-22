# Terraform::AWS::DatasyncLocationNfs

CloudFormation equivalent of aws_datasync_location_nfs

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DatasyncLocationNfs",
    "Properties" : {
        "<a href="#serverhostname" title="ServerHostname">ServerHostname</a>" : <i>String</i>,
        "<a href="#subdirectory" title="Subdirectory">Subdirectory</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#onpremconfig" title="OnPremConfig">OnPremConfig</a>" : <i>[ <a href="onpremconfig.md">OnPremConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DatasyncLocationNfs
Properties:
    <a href="#serverhostname" title="ServerHostname">ServerHostname</a>: <i>String</i>
    <a href="#subdirectory" title="Subdirectory">Subdirectory</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#onpremconfig" title="OnPremConfig">OnPremConfig</a>: <i>
      - <a href="onpremconfig.md">OnPremConfig</a></i>
</pre>

## Properties

#### ServerHostname

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subdirectory

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnPremConfig

_Required_: No

_Type_: List of <a href="onpremconfig.md">OnPremConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

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

