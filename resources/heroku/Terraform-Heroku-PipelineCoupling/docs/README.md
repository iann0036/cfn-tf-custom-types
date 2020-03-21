# Terraform::Heroku::PipelineCoupling

Provides a [Heroku Pipeline Coupling](https://devcenter.heroku.com/articles/pipelines)
resource.

A pipeline is a group of Heroku apps that share the same codebase. Once a
pipeline is created using [`heroku_pipeline`](./pipeline.html), and apps are added
to different stages using `heroku_pipeline_coupling`, you can promote app slugs
to the downstream stages.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Heroku::PipelineCoupling",
    "Properties" : {
        "<a href="#app" title="App">App</a>" : <i>String</i>,
        "<a href="#pipeline" title="Pipeline">Pipeline</a>" : <i>String</i>,
        "<a href="#stage" title="Stage">Stage</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Heroku::PipelineCoupling
Properties:
    <a href="#app" title="App">App</a>: <i>String</i>
    <a href="#pipeline" title="Pipeline">Pipeline</a>: <i>String</i>
    <a href="#stage" title="Stage">Stage</a>: <i>String</i>
</pre>

## Properties

#### App

The name of the app for this coupling.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Pipeline

The ID of the pipeline to add this app to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Stage

The stage to couple this app to. Must be one of
`review`, `development`, `staging`, or `production`.

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

#### AppId

Returns the <code>AppId</code> value.

