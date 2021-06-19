# TF::Volterra::VirtualHost CookieParamsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cookieexpiry" title="CookieExpiry">CookieExpiry</a>" : <i>Double</i>,
    "<a href="#cookierefreshinterval" title="CookieRefreshInterval">CookieRefreshInterval</a>" : <i>Double</i>,
    "<a href="#sessionexpiry" title="SessionExpiry">SessionExpiry</a>" : <i>Double</i>,
    "<a href="#authhmac" title="AuthHmac">AuthHmac</a>" : <i>[ <a href="authhmacdefinition.md">AuthHmacDefinition</a>, ... ]</i>,
    "<a href="#kmskeyhmac" title="KmsKeyHmac">KmsKeyHmac</a>" : <i>[ <a href="kmskeyhmacdefinition.md">KmsKeyHmacDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cookieexpiry" title="CookieExpiry">CookieExpiry</a>: <i>Double</i>
<a href="#cookierefreshinterval" title="CookieRefreshInterval">CookieRefreshInterval</a>: <i>Double</i>
<a href="#sessionexpiry" title="SessionExpiry">SessionExpiry</a>: <i>Double</i>
<a href="#authhmac" title="AuthHmac">AuthHmac</a>: <i>
      - <a href="authhmacdefinition.md">AuthHmacDefinition</a></i>
<a href="#kmskeyhmac" title="KmsKeyHmac">KmsKeyHmac</a>: <i>
      - <a href="kmskeyhmacdefinition.md">KmsKeyHmacDefinition</a></i>
</pre>

## Properties

#### CookieExpiry

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CookieRefreshInterval

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionExpiry

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthHmac

_Required_: No

_Type_: List of <a href="authhmacdefinition.md">AuthHmacDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyHmac

_Required_: No

_Type_: List of <a href="kmskeyhmacdefinition.md">KmsKeyHmacDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

