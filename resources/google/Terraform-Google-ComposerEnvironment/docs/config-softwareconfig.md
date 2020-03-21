# Terraform::Google::ComposerEnvironment Config SoftwareConfig

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#airflowconfigoverrides" title="AirflowConfigOverrides">AirflowConfigOverrides</a>" : <i>[ &lt;a href=&#34;config-softwareconfig-airflowconfigoverrides.md&#34;&gt;AirflowConfigOverrides&lt;/a&gt;, ... ]</i>,
    "<a href="#envvariables" title="EnvVariables">EnvVariables</a>" : <i>[ &lt;a href=&#34;config-softwareconfig-envvariables.md&#34;&gt;EnvVariables&lt;/a&gt;, ... ]</i>,
    "<a href="#imageversion" title="ImageVersion">ImageVersion</a>" : <i>String</i>,
    "<a href="#pypipackages" title="PypiPackages">PypiPackages</a>" : <i>[ &lt;a href=&#34;config-softwareconfig-pypipackages.md&#34;&gt;PypiPackages&lt;/a&gt;, ... ]</i>,
    "<a href="#pythonversion" title="PythonVersion">PythonVersion</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#airflowconfigoverrides" title="AirflowConfigOverrides">AirflowConfigOverrides</a>: <i>
      - &lt;a href=&#34;config-softwareconfig-airflowconfigoverrides.md&#34;&gt;AirflowConfigOverrides&lt;/a&gt;</i>
<a href="#envvariables" title="EnvVariables">EnvVariables</a>: <i>
      - &lt;a href=&#34;config-softwareconfig-envvariables.md&#34;&gt;EnvVariables&lt;/a&gt;</i>
<a href="#imageversion" title="ImageVersion">ImageVersion</a>: <i>String</i>
<a href="#pypipackages" title="PypiPackages">PypiPackages</a>: <i>
      - &lt;a href=&#34;config-softwareconfig-pypipackages.md&#34;&gt;PypiPackages&lt;/a&gt;</i>
<a href="#pythonversion" title="PythonVersion">PythonVersion</a>: <i>String</i>
</pre>

## Properties

#### AirflowConfigOverrides

_Required_: No
_Type_: List of &lt;a href=&#34;config-softwareconfig-airflowconfigoverrides.md&#34;&gt;AirflowConfigOverrides&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvVariables

_Required_: No
_Type_: List of &lt;a href=&#34;config-softwareconfig-envvariables.md&#34;&gt;EnvVariables&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageVersion

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PypiPackages

_Required_: No
_Type_: List of &lt;a href=&#34;config-softwareconfig-pypipackages.md&#34;&gt;PypiPackages&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PythonVersion

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

