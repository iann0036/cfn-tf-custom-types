# Terraform::Heroku::Pipeline

Provides a [Heroku Pipeline](https://devcenter.heroku.com/articles/pipelines)
resource.

A pipeline is a group of Heroku apps that share the same codebase. Once a
pipeline is created, and apps are added to different stages using
[`heroku_pipeline_coupling`](./pipeline_coupling.html), you can promote app
slugs to the next stage.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::Pipeline",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::Pipeline
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Name

The name of the pipeline.

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

