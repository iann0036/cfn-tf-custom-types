# Terraform::Google::AppEngineStandardAppVersion Handlers StaticFiles

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#applicationreadable" title="ApplicationReadable">ApplicationReadable</a>" : <i>Boolean</i>,
    "<a href="#expiration" title="Expiration">Expiration</a>" : <i>String</i>,
    "<a href="#httpheaders" title="HttpHeaders">HttpHeaders</a>" : <i>[ <a href="handlers-staticfiles-httpheaders.md">HttpHeaders</a>, ... ]</i>,
    "<a href="#mimetype" title="MimeType">MimeType</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#requirematchingfile" title="RequireMatchingFile">RequireMatchingFile</a>" : <i>Boolean</i>,
    "<a href="#uploadpathregex" title="UploadPathRegex">UploadPathRegex</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#applicationreadable" title="ApplicationReadable">ApplicationReadable</a>: <i>Boolean</i>
<a href="#expiration" title="Expiration">Expiration</a>: <i>String</i>
<a href="#httpheaders" title="HttpHeaders">HttpHeaders</a>: <i>
      - <a href="handlers-staticfiles-httpheaders.md">HttpHeaders</a></i>
<a href="#mimetype" title="MimeType">MimeType</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#requirematchingfile" title="RequireMatchingFile">RequireMatchingFile</a>: <i>Boolean</i>
<a href="#uploadpathregex" title="UploadPathRegex">UploadPathRegex</a>: <i>String</i>
</pre>

## Properties

#### ApplicationReadable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpHeaders

_Required_: No

_Type_: List of <a href="handlers-staticfiles-httpheaders.md">HttpHeaders</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MimeType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequireMatchingFile

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UploadPathRegex

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

