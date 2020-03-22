# Terraform::Template::Dir

Renders a directory containing templates into a separate directory of
corresponding rendered files.

`template_dir` is similar to [`template_file`](../d/file.html) but it walks
a given source directory and treats every file it encounters as a template,
rendering it to a corresponding file in the destination directory.

~> **Note** When working with local files, Terraform will detect the resource
as having been deleted each time a configuration is applied on a new machine
where the destination dir is not present and will generate a diff to create
it. This may cause "noise" in diffs in environments where configurations are
routinely applied by many different users or within automation systems.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Template::Dir",
    "Properties" : {
        "<a href="#destinationdir" title="DestinationDir">DestinationDir</a>" : <i>String</i>,
        "<a href="#sourcedir" title="SourceDir">SourceDir</a>" : <i>String</i>,
        "<a href="#vars" title="Vars">Vars</a>" : <i>[ <a href="vars.md">Vars</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Template::Dir
Properties:
    <a href="#destinationdir" title="DestinationDir">DestinationDir</a>: <i>String</i>
    <a href="#sourcedir" title="SourceDir">SourceDir</a>: <i>String</i>
    <a href="#vars" title="Vars">Vars</a>: <i>
      - <a href="vars.md">Vars</a></i>
</pre>

## Properties

#### DestinationDir

Path to the directory where the templated files will be written.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceDir

Path to the directory where the files to template reside.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vars

Variables for interpolation within the template. Note
that variables must all be primitives. Direct references to lists or maps
will cause a validation error.

_Required_: No

_Type_: List of <a href="vars.md">Vars</a>

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

