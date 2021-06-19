# TF::Dynatrace::HostAnomalies JavaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#outofmemory" title="OutOfMemory">OutOfMemory</a>" : <i>[ <a href="outofmemorydefinition.md">OutOfMemoryDefinition</a>, ... ]</i>,
    "<a href="#outofthreads" title="OutOfThreads">OutOfThreads</a>" : <i>[ <a href="outofthreadsdefinition.md">OutOfThreadsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#outofmemory" title="OutOfMemory">OutOfMemory</a>: <i>
      - <a href="outofmemorydefinition.md">OutOfMemoryDefinition</a></i>
<a href="#outofthreads" title="OutOfThreads">OutOfThreads</a>: <i>
      - <a href="outofthreadsdefinition.md">OutOfThreadsDefinition</a></i>
</pre>

## Properties

#### OutOfMemory

_Required_: No

_Type_: List of <a href="outofmemorydefinition.md">OutOfMemoryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OutOfThreads

_Required_: No

_Type_: List of <a href="outofthreadsdefinition.md">OutOfThreadsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

