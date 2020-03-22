# Terraform::OpenStack::ObjectstorageObjectV1

Manages a V1 container object resource within OpenStack.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenStack::ObjectstorageObjectV1",
    "Properties" : {
        "<a href="#containername" title="ContainerName">ContainerName</a>" : <i>String</i>,
        "<a href="#content" title="Content">Content</a>" : <i>String</i>,
        "<a href="#contentdisposition" title="ContentDisposition">ContentDisposition</a>" : <i>String</i>,
        "<a href="#contentencoding" title="ContentEncoding">ContentEncoding</a>" : <i>String</i>,
        "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
        "<a href="#copyfrom" title="CopyFrom">CopyFrom</a>" : <i>String</i>,
        "<a href="#deleteafter" title="DeleteAfter">DeleteAfter</a>" : <i>Double</i>,
        "<a href="#deleteat" title="DeleteAt">DeleteAt</a>" : <i>String</i>,
        "<a href="#detectcontenttype" title="DetectContentType">DetectContentType</a>" : <i>Boolean</i>,
        "<a href="#etag" title="Etag">Etag</a>" : <i>String</i>,
        "<a href="#metadata" title="Metadata">Metadata</a>" : <i>[ <a href="metadata.md">Metadata</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#objectmanifest" title="ObjectManifest">ObjectManifest</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#source" title="Source">Source</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenStack::ObjectstorageObjectV1
Properties:
    <a href="#containername" title="ContainerName">ContainerName</a>: <i>String</i>
    <a href="#content" title="Content">Content</a>: <i>String</i>
    <a href="#contentdisposition" title="ContentDisposition">ContentDisposition</a>: <i>String</i>
    <a href="#contentencoding" title="ContentEncoding">ContentEncoding</a>: <i>String</i>
    <a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
    <a href="#copyfrom" title="CopyFrom">CopyFrom</a>: <i>String</i>
    <a href="#deleteafter" title="DeleteAfter">DeleteAfter</a>: <i>Double</i>
    <a href="#deleteat" title="DeleteAt">DeleteAt</a>: <i>String</i>
    <a href="#detectcontenttype" title="DetectContentType">DetectContentType</a>: <i>Boolean</i>
    <a href="#etag" title="Etag">Etag</a>: <i>String</i>
    <a href="#metadata" title="Metadata">Metadata</a>: <i>
      - <a href="metadata.md">Metadata</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#objectmanifest" title="ObjectManifest">ObjectManifest</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#source" title="Source">Source</a>: <i>String</i>
</pre>

## Properties

#### ContainerName

A unique (within an account) name for the container.
The container name must be from 1 to 256 characters long and can start
with any character and contain any pattern. Character set must be UTF-8.
The container name cannot contain a slash (/) character because this
character delimits the container and object name. For example, the path
/v1/account/www/pages specifies the www container, not the www/pages container.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Content

A string representing the content of the object. Conflicts with
`source` and `copy_from`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentDisposition

A string which specifies the override behavior for
the browser. For example, this header might specify that the browser use a download
program to save this file rather than show the file, which is the default.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentEncoding

A string representing the value of the Content-Encoding
metadata.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentType

A string which sets the MIME type for the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CopyFrom

A string representing the name of an object
used to create the new object by copying the `copy_from` object. The value is in form
{container}/{object}. You must UTF-8-encode and then URL-encode the names of the
container and object before you include them in the header. Conflicts with `source` and
`content`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteAfter

An integer representing the number of seconds after which the
system removes the object. Internally, the Object Storage system stores this value in
the X-Delete-At metadata item.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeleteAt

An string representing the date when the system removes the object.
For example, "2015-08-26" is equivalent to Mon, Wed, 26 Aug 2015 00:00:00 GMT.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DetectContentType

If set to true, Object Storage guesses the content
type based on the file extension and ignores the value sent in the Content-Type
header, if present.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Etag

Used to trigger updates. The only meaningful value is ${md5(file("path/to/file"))}.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Metadata

_Required_: No

_Type_: List of <a href="metadata.md">Metadata</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectManifest

A string set to specify that this is a dynamic large
object manifest object. The value is the container and object name prefix of the
segment objects in the form container/prefix. You must UTF-8-encode and then
URL-encode the names of the container and prefix before you include them in this
header.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region in which to create the container. If
omitted, the `region` argument of the provider is used. Changing this
creates a new container.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

A string representing the local path of a file which will be used
as the object's content. Conflicts with `source` and `copy_from`.

_Required_: No

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

#### ContentLength

Returns the <code>ContentLength</code> value.

#### Date

Returns the <code>Date</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastModified

Returns the <code>LastModified</code> value.

#### TransId

Returns the <code>TransId</code> value.

