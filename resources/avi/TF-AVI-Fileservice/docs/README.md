# TF::AVI::Fileservice

The Fileservice resource allows the download and upload of files

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AVI::Fileservice",
    "Properties" : {
        "<a href="#localfile" title="LocalFile">LocalFile</a>" : <i>String</i>,
        "<a href="#upload" title="Upload">Upload</a>" : <i>Boolean</i>,
        "<a href="#uri" title="Uri">Uri</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AVI::Fileservice
Properties:
    <a href="#localfile" title="LocalFile">LocalFile</a>: <i>String</i>
    <a href="#upload" title="Upload">Upload</a>: <i>Boolean</i>
    <a href="#uri" title="Uri">Uri</a>: <i>String</i>
</pre>

## Properties

#### LocalFile

argument_description.
* `upload` - (Optional ) argument_description.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Upload

argument_description.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uri

argument_description.
* `local_file` - (Required) argument_description.
* `upload` - (Optional ) argument_description.

_Required_: Yes

_Type_: String

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

