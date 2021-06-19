# TF::AWS::Kinesisanalyticsv2Application CodeContentDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#textcontent" title="TextContent">TextContent</a>" : <i>String</i>,
    "<a href="#s3contentlocation" title="S3ContentLocation">S3ContentLocation</a>" : <i>[ <a href="s3contentlocationdefinition.md">S3ContentLocationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#textcontent" title="TextContent">TextContent</a>: <i>String</i>
<a href="#s3contentlocation" title="S3ContentLocation">S3ContentLocation</a>: <i>
      - <a href="s3contentlocationdefinition.md">S3ContentLocationDefinition</a></i>
</pre>

## Properties

#### TextContent

The text-format code for the application.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3ContentLocation

_Required_: No

_Type_: List of <a href="s3contentlocationdefinition.md">S3ContentLocationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

