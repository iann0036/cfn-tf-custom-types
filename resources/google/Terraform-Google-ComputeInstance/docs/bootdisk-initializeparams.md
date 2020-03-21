# Terraform::Google::ComputeInstance BootDisk InitializeParams

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="bootdisk-initializeparams-labels.md">Labels</a>, ... ]</i>,
    "<a href="#size" title="Size">Size</a>" : <i>Double</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="bootdisk-initializeparams-labels.md">Labels</a></i>
<a href="#size" title="Size">Size</a>: <i>Double</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### Image

The image from which to initialize this disk. This can be
one of: the image's `self_link`, `projects/{project}/global/images/{image}`,
`projects/{project}/global/images/family/{family}`, `global/images/{image}`,
`global/images/family/{family}`, `family/{family}`, `{project}/{family}`,
`{project}/{image}`, `{family}`, or `{image}`. If referred by family, the
images names must include the family name. If they don't, use the
[google_compute_image data source](/docs/providers/google/d/datasource_compute_image.html).
For instance, the image `centos-6-v20180104` includes its family name `centos-6`.
These images can be referred by family name here.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="bootdisk-initializeparams-labels.md">Labels</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

The size of the image in gigabytes. If not specified, it
will inherit the size of its base image.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The GCE disk type. May be set to pd-standard or pd-ssd.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

